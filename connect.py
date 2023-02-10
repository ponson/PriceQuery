import requests
from bs4 import BeautifulSoup


resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)
print(soup.find(id='mac-p'))
print(soup.find('', {'data-foo':'mac-foo'}))