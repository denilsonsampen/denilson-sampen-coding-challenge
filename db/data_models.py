# Import SQLAlchemy classes
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# We create an instance of the SQLAlchemy Base class to declare the necessary three tables
Base = declarative_base()

# We define the Departments class to represent the 'departments.csv' table
class Departments(Base):
    __tablename__ = 'departments'   # Table name
    
    # We define column tables
    id = Column(Integer, primary_key=True)
    department = Column(String)

# We define the Jobs class to represent the 'jobs.csv' table
class Jobs(Base):
    __tablename__ = 'jobs'   # Table name

    # We define column tables
    id = Column(Integer, primary_key=True)
    job = Column(String)

# We define the HiredEmployees class to represent the 'hired_employees.csv' table
class HiredEmployees(Base):
    __tablename__ = 'hired_employees'   # Table name

    # We define column tables
    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('departments.id'))   # Related to departments table
    job_id = Column(Integer, ForeignKey('jobs.id')) # Related to jobs table