# Import module for DB creation and data structure from db_creation.py
from sqlalchemy import create_engine
from data_models import Base

# Define DB URL
DB_URL = 'sqlite:///db.globant_db'
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

# We print if successful
print("Globant database created successfully")