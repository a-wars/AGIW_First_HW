# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class Test3Spider(CrawlSpider):
    name = 'test3'
    allowed_domains = ['www.dia.uniroma3.it']
    start_urls = ['http://www.dia.uniroma3.it/~patrigna/photos/index.html']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tag_num = len(soup.find_all())
        yield {
            "url": response.url,
            "tags": tag_num
        }