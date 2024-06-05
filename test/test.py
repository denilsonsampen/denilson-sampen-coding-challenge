import requests

url = 'http://127.0.0.1:5000/upload_csv'
files = {'file': open('./data/departments.csv', 'rb')}
response = requests.post(url, files=files)

print(response.text)