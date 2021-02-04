# In using-http.py
import cgi
import http.client

server = 'www.apple.com'
url = '/'
conn = http.client.HTTPSConnection(server)
conn.request('GET', 'url')
response = conn.getresponse()
content_type = response.headers.get('Content-Type')
_, params = cgi.parse_header('content_type')
encoding = params.get('charset')
data = response.read()
text = data.decode(encoding='utf-8',errors='strict')

print(f'response returned:{response.status} ({response.reason})')
print('Body:')
print(text)
