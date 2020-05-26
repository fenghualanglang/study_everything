# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from MyScrapy.items import MyscrapyItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    base_url = 'https://movie.douban.com/top250'


    # def start_requests(self):
    # 	# 使用这个上面start_urls 可以注销, dont_filter=True  下面列表去重
    # 	start_urls = ['https://movie.douban.com/top250']
    # 	yield scrapy.Request(url=link, callback=self.detile_parse, dont_filter=True)

    def parse(self, response):
        tops = response.xpath('//div[@class="item"]')
        for html in tops:
            item = MyscrapyItem()
            item['quote'] = html.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract_first()
            item['score'] = html.xpath('.//span[@class="rating_num"]/text()').extract_first()
            item['comment'] = html.xpath('.//div[@class="star"]/span[last()]/text()').extract_first()
            link = html.xpath('.//div[@class="hd"]/a/@href').extract_first()
            yield scrapy.Request(url=link, callback=self.detile_parse, meta={'key': item})

        next_url = response.xpath('//*[text()="后页>"]/@href').extract_first()
        if next_url is not None:
            next_url = urljoin(self.base_url, next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def detile_parse(self, response):

        item = response.meta['key']
        move_name = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        director = response.xpath('//*[text()="导演"]/following-sibling::span/a/text()').extract_first()
        screen_writer = '/'.join(response.xpath('//*[text()="编剧"]/following-sibling::span/a/text()').extract())
        to_star = ''.join(response.xpath('//*[text()="主演"]/following-sibling::span//text()').extract())
        type = '/'.join(response.xpath('//*[@property="v:genre"]/text()').extract())
        # area = response.xpath('//*[@id="info"]/text()[2]').extract()
        # language = response.xpath('//*[@id="info"]/text()[3]').extract()
        publish = '/'.join(response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract())
        runtime = '/'.join(response.xpath('//*[@property="v:runtime"]/text()').extract())
        img_src = response.xpath('//*[@id="mainpic"]/a/img/@src').extract_first()
        url = response.url
        # css 选择器
        # name = response.css('title::text').extract_first()

        item['move_name'] = move_name
        item['director'] = director
        item['screen_writer'] = screen_writer
        item['to_star'] = to_star
        item['type'] = type
        item['publish'] = publish
        item['runtime'] = runtime
        item['url'] = url
        item['image_urls'] = img_src
        yield item

'''
from urllib.parse import urljoin
category_link = urljoin(self.base_url, category.xpath('./td/p[@class="tags  tag-first "]/a/@href').extract_first())


from urllib.parse import urlencode
from requests.exceptions import RequestException
    data = {
        'offset': offset,
        'keyword': keyword
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)

def start_requests(self):
    # 构建url
    url = self.start_urls[0]
    # 构建post_data
    post_data = {
        'email': '',
        'password': ''
    }
    # 发送post请求
    yield scrapy.FormRequest(url=url, formdata=post_data)

'''



