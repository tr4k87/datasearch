from lxml import html
import requests
from pprint import pprint
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

url = 'https://www.ebay.com'
responce = requests.get(url + '/b/Wristwatches/31387/bn_2408451', headers=header)
dom = html.fromstring(responce.text)

items_list = []
items = dom.xpath("//li[@class='s-item s-item--large']")
for i in items:
    item_info = {}
    name = i.xpath(".//h3[@class='s-item__title']/text()")
    link = i.xpath(".//h3[@class='s-item__title']/../@href") 
    price = i.xpath(".//span[@class= 's-item__price']//text()")

    item_info['name'] = name
    item_info['link'] = link
    item_info['price'] = price
    items_list.append(item_info)

df = pd.DataFrame(items_list)
df.to_csv('result.csv')
print(len(items_list))

