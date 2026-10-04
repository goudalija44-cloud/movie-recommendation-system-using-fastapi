import requests

url = "http://127.0.0.1:8000/recommend"

data = {
   "movie": ""
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")

print(response.json())