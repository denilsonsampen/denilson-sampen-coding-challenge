# Import SQLAlchemy classes
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the SQLAlchemy Base class to declare the necessary three tables
Base = declarative_base()