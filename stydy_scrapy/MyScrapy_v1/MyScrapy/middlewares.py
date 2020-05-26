from MyScrapy.settings import USER_AGENT_LIST
from fake_useragent import UserAgent

class UserAgentMilldewares(object):

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua
        # request.headers.setdefault('User-Agent', UserAgent().chrome)


from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class SeliniumMilldewares(object):

    '''
    判断url某个参数是否在里面，或者判断响应状态码进行打码
        与前面信号合用
    '''
    def process_request(self, request, spider):

        if 'wiki' in request.url:
            spider.driver.get(request.url)
            # self.driver.find_elements_by_xpath('//div[@class="wiki-tag"]/a/@href').click()
            page_source = spider.driver.page_source
            response = HtmlResponse(url=request.url, request=request, body=page_source.encode(), encoding="utf-8",)
            return response



import random
from MyScrapy.settings import PROXY_LIST

class RandomProxy(object):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = self.get_random_proxy()
        print("this is ip:"+thisip["IP"] + ':' + thisip["Port"])
        request.meta["proxy"]= "http://"+thisip["IP"] + ':' + thisip["Port"]


    # def process_response(self, request, response, spider):
    #     '''对返回的response处理'''
    #     #  如果返回的response状态不是200，重新生成当前request对象  
    #     if response.status == 200:
    #         proxy = self.get_random_proxy()
    #         # print("this is response ip:" + proxy)
    #         #  对当前reque加上代理  
    #         request.meta['proxy'] = proxy
    #     return response

    def get_random_proxy(self):
        thisip=random.choice(PROXY_LIST)
        return thisip
