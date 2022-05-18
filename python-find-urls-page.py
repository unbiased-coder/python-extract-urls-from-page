import requests

from bs4 import BeautifulSoup

page = 'https://www.google.com'

print (f'Downloading page: {page}')
res = requests.get(page)

print (f'Got back response: {res.status_code}')
print (f'Page length: {len(res.text)}')
html = res.text
bs = BeautifulSoup(html, features='html.parser')
hrefs = bs.find_all('a')
for href in hrefs:
    print (f'Found URL: {href.get("href")}')
