# -*- coding: utf-8 -*-

'''
此爬虫是聚合信号与selenium
    信号是在selenium 访问后自动关闭
'''


import scrapy
from scrapy import signals
from selenium import webdriver

class BaiduSpider(scrapy.Spider):

    name = 'guazi2'
    allowed_domains = ['guazi.com']
    # start_urls = ['https://www.guazi.com/bj/buy/']


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.driver = webdriver.Chrome()
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
        spider.driver.quit()

    def start_requests(self):
        yield scrapy.Request('https://www.guazi.com/bj/buy/', callback=self.parse)

    def parse(self, response):
        # print(response.text)

        pass



