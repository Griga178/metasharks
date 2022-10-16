import requests

url = 'http://localhost:8000/api/salesmanager/'
response = requests.get(url)

response_on_python = response.json()

for row in response_on_python:
    print(row)

url = 'http://localhost:8000/api/colors/'
response = requests.get(url)

response_on_python = response.json()

for row in response_on_python:
    print(row)

url = 'http://localhost:8000/api/brands/'
response = requests.get(url)

response_on_python = response.json()

for row in response_on_python:
    print(row)

url = 'http://localhost:8000/api/models/'
response = requests.get(url)

response_on_python = response.json()

for row in response_on_python:
    print(row)
