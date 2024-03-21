import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
import pandas as pd

class HhruSpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = ["https://www.ebay.com/b/Seiko-Watches/31387/bn_2999799?LH_ItemCondition=1000&rt=nc&_udlo=20%C2%A0350&_udhi=38%C2%A0350&mag=1"]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@data-qa = 'pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class= 's-item__link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath("//h1//text()").getall()
        price = response.xpath("//div[@class= 'x-price-primary']//text()").get()
        url = response.url
        _id = response.xpath("//span[@xpath='1']//text")
        yield{'name': name, 'price':price, 'url':url, 'id':_id}


