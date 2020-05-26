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
from scrapy.utils.project import get_project_settings
import os
import scrapy


class ImagePipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        return scrapy.Request(url=item['img_src'])

    def item_completed(self, results, item, info):

        try:
            images = [data['path'] for ok, data in results if ok]
            old_name = self.IMAGES_STORE + os.sep + images[0]
            new_name = self.IMAGES_STORE + os.sep + images[0].split(os.sep)[0] + os.sep + item['move_name'] + '.png'

            # 重命名
            os.rename(old_name, new_name)
            item['image_path'] = new_name

            return item
        except:
            pass

        # Define your item pipelines here
        #
        # Don't forget to add your pipeline to the ITEM_PIPELINES setting
        # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
        import pymysql



class MyscrapyPipeline:
    def process_item(self, item, spider):
        return item




from databases.MysqlModels import Douban

class MySQLPipeline(object):

    def process_item(self, item, spider):

        Douban.create(**item)
        return item

























