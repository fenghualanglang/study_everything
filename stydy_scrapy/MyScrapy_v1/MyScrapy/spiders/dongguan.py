# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from Sun.items import SunItem

class DongguanSpider(CrawlSpider):
    name = 'tencent'
    # 修改允许的域
    allowed_domains = ['tencent.com']
    # 修改起始的url
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 构建翻页用的规则
        Rule(LinkExtractor(allow=r'position.php\?&start=\d+#a'), follow=True),
        Rule(LinkExtractor(allow=r'position_detail'), callback='parse_item'),
    )

    def parse_item(self, response):
        # print('----',response.url)
        item = SunItem()

        item['name'] = response.xpath('//*[@id="sharetitle"]/text()').extract_first()
        item['url'] = response.url
        item['category'] = response.xpath('//tr[2]/td[2]/text()').extract_first()
        item['address'] = response.xpath('//tr[2]/td[1]/text()').extract_first()
        item['num'] = response.xpath('//tr[2]/td[3]/text()').extract_first()

        yield item