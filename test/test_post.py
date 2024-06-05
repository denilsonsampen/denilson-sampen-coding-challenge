import requests

# Define the URL for the API endpoint
url = 'http://127.0.0.1:5000/upload_csv'

# Open the CSV file
files = {'file': open('./data/jobs.csv', 'rb')} # This can be change from departments, jobs and hired_employees

# Define the form data to specify table name
data = {'table': 'jobs'}    # Has to match CSV file name

# Make a POST request to the API endpoint with the CSV file and form data
response = requests.post(url, files=files, data=data)

# Print the response
print(response.text)