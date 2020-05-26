# -*- coding: utf-8 -*-
from MyScrapy.settings import USER_AGENT_LIST
from fake_useragent import UserAgent

class UserAgentMilldewares(object):

    def process_request(self, request, spider):
        # ua = random.choice(USER_AGENT_LIST)
        # request.headers['User-Agent'] = ua
        request.headers.setdefault('User-Agent', UserAgent().chrome)

from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class SeliniumMilldewares(object):

    '''
    判断url某个参数是否在里面，或者判断响应状态码进行打码
    '''
    def process_request(self, request, spider):

        if 'wiki' in request.url:
            driver = webdriver.Chrome()  #options=opt
            driver.get(request.url)

            time.sleep(3)

            print("访问:{0}".format(request.url))

            driver.find_elements_by_xpath('//div[@class="wiki-tag"]/a/@href').click()

            time.sleep(2)

            page_source = driver.page_source

            print("访问:{0}".format(request.url))

            response = HtmlResponse(url=request.url, request=request, body=page_source.encode(), encoding="utf-8",)
            driver.quit()

            return response


import random
from MyScrapy.settings import PROXY_LIST

class ProxyMilldewares(object):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        try:
            thisip=random.choice(PROXY_LIST)
            request.meta["proxy"]= "http://"+thisip["IP"] + ':' + thisip["Port"]
        except Exception as e:
            print(e)






