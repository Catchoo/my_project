# -*- coding: utf-8 -*-
import scrapy

"""太白的诗"""


class TaibaiSpider(scrapy.Spider):
    name = 'taibai'
    allowed_domains = ['www.gushiwen.org']
    start_urls = ['https://www.gushiwen.org/shiwen/default_2A247A1.aspx']

    def parse(self, response):
        item = {}

        # 列表页分组
        son_list = response.xpath('//div[@class="left"]/div[@class="sons"]')
        for son in son_list:
            item["title"] = son.xpath('./div[1]/p[1]/a/b/text()').extract_first()
            # pr(title)
            item["dynasty"] = son.xpath('./div[1]/p[2]/a[1]/text()').extract_first()
            item["author"] = son.xpath('./div[1]/p[2]/a[2]/text()').extract_first()
            # print(author)
            # print(dynasty)
            item["content"] = son.xpath('./div[1]/div[@class="contson"]/text()').extract()
            print(item["content"])  # divr[constson]有的时候还有1-2个p子标签.目前的办法是两种匹配方式扫两边,最后数据再做汇总

            yield item
        # 翻页
        # print(11111)
        next_url = str(response.xpath('//*[@id="FromPage"]/div/a[1]/@href').extract()[0])
        # "//*[@id="FromPage"]/div/a[1]"
        # 判断是否为最后一页
        if next_url:

            next_url = "https://www.gushiwen.org"+next_url
            # print(next_url)
            yield scrapy.Request(next_url,callback=self.parse,method='GET')

