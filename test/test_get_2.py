import requests

#url = 'http://127.0.0.1:5000/employees_by_job_department_2021'
url = 'http://127.0.0.1:5000/departments_above_average'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
