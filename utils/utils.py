# Import libraries
import pandas as pd

# Function to read csv files
def read_csv(file_path):
    return pd.read_csv(file_path,header=None)