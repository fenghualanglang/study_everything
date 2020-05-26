# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



import json
import pymysql

class MyscrapyWritePipeline(object):

    def open_spider(self, spider):
        self.file = open('liebiao.json', 'w')

    def process_item(self, item, spider):
        dict_data = dict(item)
        str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()



from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, meta={'image_name': item['image_name']})

    def file_path(self, request, response=None, info=None):

        file_name = request.meta['image_name']

        return file_name

    def item_completed(self, results, item, info):
        pass

from databases.MysqlModels import Douban

class MySQLPipeline(object):

    def process_item(self, item, spider):

        Douban.create(**item)
        return item




import pymongo


class MongoPipeline(object):

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()


    def process_item(self, item, spider):

        self.client.douban.move_name.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()

# 分布式爬虫
from datetime import datetime

class DoubanPipeline(object):
    def process_item(self, item, spider):
        # #utcnow() 是获取UTC时间
        # item["crawled"] = datetime.utcnow()
        # # 爬虫名
        # item["spider"] = spider.name
        return item





















