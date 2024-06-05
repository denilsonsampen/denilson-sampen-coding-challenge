from flask import Flask, request, jsonify
from utils.utils import read_csv
from db.data_models import Departments, Jobs, HiredEmployees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd

app = Flask(__name__)

app = Flask(__name__)

# Database configuration
DB_URL = 'sqlite:///../db.globant_db'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        data = read_csv(file)
        table_name = request.form['table']

        if table_name == 'departments':
            with Session() as session:
                for index, row in data.iterrows():                
                    session.add(Departments(id=row[0], department=row[1]))
                session.commit()
        elif table_name == 'jobs':
            with Session() as session:
                for index, row in data.iterrows():                 
                    session.add(Jobs(id=row[0], job=row[1]))
                session.commit()
        elif table_name == 'hired_employees':
            with Session() as session:
                for index, row in data.iterrows():
                    session.add(HiredEmployees(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4]))
                session.commit()
        else:
            return jsonify({'error': 'Invalid table name'}), 400
        
        return jsonify({'message': 'Data uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)