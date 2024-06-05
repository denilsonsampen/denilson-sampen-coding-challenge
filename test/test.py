import requests

url = 'http://127.0.0.1:5000/upload_csv'
files = {'file': open('./data/hired_employees.csv', 'rb')}
data = {'table': 'hired_employees'}
response = requests.post(url, files=files, data=data)


print(response.text)