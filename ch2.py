import requests
from bs4 import BeautifulSoup


resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h3').text)
print(soup.find(id='mac-p'))
print(soup.find('', {'data-foo':'mac-foo'}))