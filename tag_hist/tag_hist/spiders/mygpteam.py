# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class MygpteamSpider(CrawlSpider):
    name = 'mygpteam'
    allowed_domains = ['www.unieuro.it']
    start_urls = ['https://www.unieuro.it/online/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tag_num = len(soup.find_all())
        yield {
            "url": response.url,
            "tags": tag_num
        }