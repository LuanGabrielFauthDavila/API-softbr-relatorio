import requests
import json


url = 'http://127.0.0.1:8000/?key=123456'
data = {
  'key': "123456",
}

r = requests.get(url)
print(r.json())