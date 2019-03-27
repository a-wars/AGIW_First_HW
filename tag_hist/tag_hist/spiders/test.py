# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TestSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['www.dia.uniroma3.it']
    start_urls = ['http://www.dia.uniroma3.it/~patrigna/photos/index.html']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]


    def parse_item(self, response):
        yield {
                'url': response.url,
                'src': response.text
        }