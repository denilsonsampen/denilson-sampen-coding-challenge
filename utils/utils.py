# Import libraries
import pandas as pd

# Function to read csv files
def read_csv(file_path):
    return pd.read_csv(file_path,header=None)

# Function to insert batch of data into database
def insert_batch(session, model, batch):
    session.bulk_save_objects(batch)
    session.commit()