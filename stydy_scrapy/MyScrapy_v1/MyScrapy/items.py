# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    move_name = scrapy.Field()
    director = scrapy.Field()
    screen_writer = scrapy.Field()
    to_star = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    publish = scrapy.Field()
    url = scrapy.Field()
    comment = scrapy.Field()
    score = scrapy.Field()
    quote = scrapy.Field()
    runtime = scrapy.Field()
    image_urls = scrapy.Field()


class SunItem(scrapy.Item):
    pass
