# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['www.tldp.org/LDP/']
    start_urls = ['http://www.tldp.org/LDP/abs/html/why-shell.html',
                  'http://www.tldp.org/LDP/abs/html/quoting.html']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tag_num = len(soup.find_all()) #no of tags
        yield {
            "url": response.url,
            "tags": tag_num
        }
