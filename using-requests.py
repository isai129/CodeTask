# In using-requests.py
import requests

url = 'http://192.254.76.124:88'
requests = requests.get(url)
print(f'Response returned: {response.ststus_code}, {requests.status_code}, {requests.reason}')
print(response.txt)
