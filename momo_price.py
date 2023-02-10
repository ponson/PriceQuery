import requests
from bs4 import BeautifulSoup


# resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/blog/blog.html')

USER_AGENT_VALUE = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
headers = {'user-agent': USER_AGENT_VALUE}
resp = requests.get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10363229&Area=search&mdiv=403&oid=1_3&cid=index&kw=saucony', headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
metas = soup.find_all('meta', property="product:price:amount")
for m in metas:
    print(m['content'])
    print(type(m))