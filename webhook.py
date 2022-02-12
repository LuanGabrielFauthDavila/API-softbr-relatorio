import requests
import json


url = 'https://api-softbr-relatorios.herokuapp.com/?key=123456'
data = {
  'key': "123456",
}

r = requests.get(url)
print(r.json())