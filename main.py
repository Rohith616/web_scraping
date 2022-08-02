import requests
from bs4 import BeautifulSoup

url = 'https://www.moe.gov.sg/private-education/private-schools'

res = requests.get(url)
print(res.status_code)
doc = BeautifulSoup(res.text,'html.parser')
print(doc.title.text)
print(doc)