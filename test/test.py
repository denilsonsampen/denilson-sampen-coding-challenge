import requests

url = 'http://127.0.0.1:5000/upload_csv'
files = {'file': open('./data/jobs.csv', 'rb')}
data = {'table': 'jobs'}
response = requests.post(url, files=files, data=data)


print(response.text)