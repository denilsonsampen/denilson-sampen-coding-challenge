from flask import Flask, request, jsonify
from utils.utils import read_csv, insert_batch
from db.data_models import Departments, Jobs, HiredEmployees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database configuration
DB_URL = 'sqlite:///../db.globant_db'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

# Maximum number of rows to process per batch
MAX_BATCH_SIZE = 1000

# Define API POST method
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
        
        return jsonify({'message': 'Data uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)