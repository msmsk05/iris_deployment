import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={"sepal_length":5.1, "sepal_width":3.5, "petal_length":1.4, "petal_width":0.2})

print(r.json())