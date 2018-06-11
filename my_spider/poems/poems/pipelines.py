# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from pymongo import MongoClient

# class PoemsPipeline(object):
#
#     def open_spider(self,spider):
#         mongo = MongoClient(host="127.0.0.1",port=27017)
#         self.db=mongo.poems.taibai
#         pass
#
#     def process_item(self, item, spider):
#         self.db.insert(dict(item))
#
#
#
#         return item


class FileWritepipeline(object):

    def open_spider(self,spider):
        self.f = open("poemfile.txt",'a',encoding="utf-8")

    def process_item(self,item,spider):
        # print("管道里的{}".format(item))
        self.f.write(json.dumps(dict(item), ensure_ascii=False, indent=2) + ',\n')
        return item  # 不return的情况下，另一个权重较低的pipeline将不会获得item

    def close_spider(self,spider):
        self.f.close()