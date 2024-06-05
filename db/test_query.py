from flask import Flask, request, jsonify
#from utils.utils import read_csv, insert_batch
from data_models import Departments, Jobs, HiredEmployees
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import func, Integer
import os

# Obtener la ruta absoluta al archivo de base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '../db.globant_db')

# Crear la URL de la base de datos
DB_URL = f'sqlite:///{DB_PATH}'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

# Establish the session
session = Session()

# Construct the SQL query
query = session.query(
    Departments.department,
    Jobs.job,
    func.sum(func.cast(func.strftime('%m', HiredEmployees.datetime).between('01', '03'), Integer)).label('Q1'),
    func.sum(func.cast(func.strftime('%m', HiredEmployees.datetime).between('04', '06'), Integer)).label('Q2'),
    func.sum(func.cast(func.strftime('%m', HiredEmployees.datetime).between('07', '09'), Integer)).label('Q3'),
    func.sum(func.cast(func.strftime('%m', HiredEmployees.datetime).between('10', '12'), Integer)).label('Q4')
).join(HiredEmployees, Departments.id == HiredEmployees.department_id).join(Jobs, Jobs.id == HiredEmployees.job_id).filter(
    func.strftime('%Y', HiredEmployees.datetime) == '2021'
).group_by(
    Departments.department,
    Jobs.job
).order_by(
    Departments.department.asc(),
    Jobs.job.asc()
)

# Execute the query and fetch results
results = query.all()

# Close the session
session.close()

# Format the results into a pandas DataFrame
df = pd.DataFrame(results, columns=['department', 'job', 'Q1', 'Q2', 'Q3', 'Q4'])

# Print the DataFrame
print(df)