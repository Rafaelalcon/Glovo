import urllib.parse

with open('api_key.txt') as file:
    key = file.read()

API_KEY = key

def get_scraperapi_url(url):
    if 1 == 1:
        payload = {'api_key': API_KEY, 'url': url}
        proxy_url = 'http://api.scraperapi.com/?' + urllib.parse.urlencode(payload)
    else: 
        proxy_url = url
    return proxy_url