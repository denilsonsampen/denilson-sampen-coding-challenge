from flask import Flask, request, jsonify
from utils.utils import read_csv, insert_batch
from db.data_models import Departments, Jobs, HiredEmployees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, text
import os

app = Flask(__name__)

# Database configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '../db.globant_db')
DB_URL = f'sqlite:///{DB_PATH}' # Create the database URL for SQLite
engine = create_engine(DB_URL)  # Create the database engine
Session = sessionmaker(bind=engine) # Create the database session

# Maximum number of rows to process per batch
MAX_BATCH_SIZE = 1000

# Define API POST method for upload CSV data
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        # Read CSV file from request
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        # Read CSV to Dataframe
        data = read_csv(file)
        table_name = request.form['table']

        # Insert data per batch
        batch = []
        with Session() as session:
            for index, row in data.iterrows():
                # Create model instance by table name
                if table_name == 'departments':      
                    model = Departments(id=row[0], department=row[1])
                elif table_name == 'jobs':
                    model = Jobs(id=row[0], job=row[1])
                elif table_name == 'hired_employees':
                    model = HiredEmployees(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4])
                else:
                    return jsonify({'error': 'Invalid table name'}), 400
                
                # Append model to batch
                batch.append(model)

                # Insert batch if size exceeds MAX_BATCH_SIZE
                if len(batch) >= MAX_BATCH_SIZE:
                    insert_batch(session, model.__class__, batch)
                    batch = []
            
            # Insert remaining batch
            if batch:
                insert_batch(session, model.__class__, batch)
        
        return jsonify({'message': 'Data uploaded successfully'}), 200  # Return a success message

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if an exception occurs

# Define API GET method for employees hired in 2021 by job, department and quarter
@app.route('/employees_by_job_department_2021', methods=['GET'])
def employees_by_job_department_2021():
    try:
        session = Session()
        
        # Query to get employees hired in 2021 by job, department and quarter
        query = text("""
            SELECT d.department AS department,j.job AS job, 
                     COUNT(CASE WHEN strftime('%m', h.datetime) BETWEEN '01' AND '03' THEN 1 END) AS Q1,
                     COUNT(CASE WHEN strftime('%m', h.datetime) BETWEEN '04' AND '06' THEN 1 END) AS Q2,
                     COUNT(CASE WHEN strftime('%m', h.datetime) BETWEEN '07' AND '09' THEN 1 END) AS Q3,
                     COUNT(CASE WHEN strftime('%m', h.datetime) BETWEEN '10' AND '12' THEN 1 END) AS Q4
                     FROM hired_employees h
                     LEFT JOIN departments d
                     ON h.department_id = d.id
                     LEFT JOIN jobs j
                     ON h.job_id = j.id
                     WHERE strftime('%Y', h.datetime) = '2021'
                     GROUP BY h.department_id, h.job_id
                     ORDER BY department ASC, job ASC;
        """)
        
        result = session.execute(query) # Execute the query
        data = result.fetchall()    # Fetch all the results
        columns = result.keys()     # Get the column names
        results = [dict(zip(columns, row)) for row in data] # Convert results to a list of dictionaries
        return jsonify(results), 200    # Return the results as JSON

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if an exception occurs

# Define API GET method for departments above average hire count in 2021
@app.route('/departments_above_average', methods=['GET'])
def departments_above_average():
    try:
        session = Session()

        # Query to get departments above average hire count in 2021
        query = text("""
                WITH department_hire_counts AS (
                    SELECT 
                        department_id,
                        COUNT(*) AS hired
                    FROM hired_employees
                    WHERE strftime('%Y', datetime) = '2021'
                    GROUP BY department_id
                ),
                average_hire_count AS (
                    SELECT 
                        AVG(hired) AS avg_hire_count
                    FROM department_hire_counts
                )
                SELECT 
                    d.id,
                    d.department,
                    dhc.hired
                FROM departments d
                JOIN department_hire_counts dhc ON d.id = dhc.department_id
                WHERE dhc.hired > (SELECT avg_hire_count FROM average_hire_count)
                ORDER BY dhc.hired DESC;
            """)
        
        result = session.execute(query) # Execute the query
        data = result.fetchall()    # Fetch all the results
        columns = result.keys()     # Get the column names
        results = [dict(zip(columns, row)) for row in data] # Convert results to a list of dictionaries
        return jsonify(results), 200    # Return the results as JSON
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if an exception occurs

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application in debug mode