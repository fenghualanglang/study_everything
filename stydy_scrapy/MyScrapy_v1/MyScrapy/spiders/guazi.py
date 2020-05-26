# -*- coding: utf-8 -*-

'''
Splash是一个JavaScript渲染服务，是一个带有HTTP API的轻量级浏览器，同时它对接了Python中的Twisted和QT库。
利用它，我们同样可以实现动态渲染页面的抓取。

异步方式处理多个网页渲染过程；
获取渲染后的页面的源代码或截图；
通过关闭图片渲染或者使用Adblock规则来加快页面渲染速度；
可执行特定的JavaScript脚本；
可通过Lua脚本来控制页面渲染过程；
获取渲染的详细过程并通过HAR（HTTP Archive）格式呈现。
接下来，我们来了解一下它的具体用法。
'''


import scrapy
from scrapy_splash import SplashRequest

class BaiduSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']

    def start_requests(self):
        lua_script = '''
            function main(splash)
                splash:go("https://www.guazi.com/bj/buy/")
                splash:wait(2)
                return splash:html()
            end
            '''
        yield SplashRequest('https://www.guazi.com/bj/buy/', callback=self.parse, endpoint='execute', args={'lua_source': lua_script})

    def parse(self, response):
        print(response.text)
        # with open('tt.html', 'wb') as f:
        #     f.write(response.content.decode("utf-8"))
        pass
