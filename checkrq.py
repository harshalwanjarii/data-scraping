import requests
r = requests.get('https://www.httpbin.org/get')
r.text

print(r.text)

r = requests.post('https://www.httpbin.org/post')

r.text

print(r.url)