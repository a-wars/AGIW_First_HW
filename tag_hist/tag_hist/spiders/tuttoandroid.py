# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tag_hist.utils.bitset_html import to_bit_array
from tag_hist.utils.count_tags import count_tags

class TuttoandroidSpider(CrawlSpider):
    name = 'tuttoandroid'
    allowed_domains = ['www.tuttoandroid.net']
    start_urls = ['https://www.tuttoandroid.net']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        src = response.text
        result = {'url': response.url}
        tag_num = count_tags(src)
        result.update({'tags': tag_num})
        bitset = to_bit_array(src, 64, 2048)
        #bitset = bitset.tolist()
        #bitset_dict = {index : value for index, value in enumerate(bitset)}
        for index, value in enumerate(bitset):
            if value:
                result.update({index: 1})
            else:
                result.update({index: 0})        
        yield result
