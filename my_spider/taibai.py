# -*- coding: utf-8 -*-
import scrapy


class TaibaiSpider(scrapy.Spider):
    name = 'taibai'
    allowed_domains = ['xx.cn']
    start_urls = ['http://xx.cn/']

    def parse(self, response):
        pass
