import requests
from bs4 import BeautifulSoup

r = requests.get('https://read.qidian.com/chapter/apThsB8Y9w1fNVrkjhr67g2/DTjjaq3PgEaaGfXRMrUjdw2')
# h = r.headers
# print(h)

html_doc = r.text
# print(html_doc)
soup = BeautifulSoup(html_doc,'html.parser')
txt = soup.get_text()
print(txt)
