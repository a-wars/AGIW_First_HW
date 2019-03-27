# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BookingSpider(CrawlSpider):
    name = 'booking'
    allowed_domains = ['www.booking.com']
    start_urls = ['http://www.booking.com/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        yield {
            "url": response.url,
            "tags": response.text
        }