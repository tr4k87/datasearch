from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse

url = 'https://books.toscrape.com/'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find_all('li', ('class', 'col-xs-6 col-sm-4 col-md-3 col-lg-3'))
url_1 = 'https://books.toscrape.com/'
url_2 = []
url_2 = []
for i in result:
    i.find_all('li', ('class', 'col-xs-6 col-sm-4 col-md-3 col-lg-3'))
    url_2.append(i.find('a').get('href'))
url_j = []
for link in url_2:
    url_j.append(urllib.parse.urljoin(url_1, link))
first = url_j[0]
response = requests.get(first)
soup = BeautifulSoup(response.content, 'html.parser')
# name = soup.find('li', ('class', 'active')).text
# price = soup.find('p', ('class', 'price_color')).text
# print(name, price)

name =[]
price =[]
instock = []
output ={}


for i in url_j:
  response = requests.get(i)
  soup = BeautifulSoup(response.content, 'html.parser')


  try:
    name.append(soup.find('li', ('class', 'active')).text)
  except:
    name.append('')

 
  try:
    p = soup.find('p', ('class', 'price_color')).text
    price.append(p)
  except:
    price.append('')


  try:
    instock.append(soup.find('p', ('class', 'instock availability')).text)
  except:
    instock.append('')


  output = {'Name' : name, 'Price' : price, 'Instock' : instock}
  
df = pd.DataFrame(output)
print(df)


