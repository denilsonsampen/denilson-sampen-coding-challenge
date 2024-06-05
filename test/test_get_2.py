import requests

# Define the URL for the API endpoint
url = 'http://127.0.0.1:5000/departments_above_average'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and print it
    data = response.json()
    print(data)
else:
    # Print an error message if the request failed
    print('Error:', response.status_code)
