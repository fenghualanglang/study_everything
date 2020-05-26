
'''
Splash是一个JavaScript渲染服务，是一个带有HTTP API的轻量级浏览器，同时它对接了Python中的Twisted和QT库。
利用它，我们同样可以实现动态渲染页面的抓取

    异步方式处理多个网页渲染过程；
    获取渲染后的页面的源代码或截图；
    通过关闭图片渲染或者使用Adblock规则来加快页面渲染速度；
    可执行特定的JavaScript脚本；
    可通过Lua脚本来控制页面渲染过程；
    获取渲染的详细过程并通过HAR（HTTP Archive）格式呈现。
'''

import requests

from fake_useragent import UserAgent
from urllib.parse import quote

#  render.html 此接口获取javascrapt 页面渲染的代码
splash_url = 'http://192.168.43.188:8050/render.html?url={}&wait=3'

#  render.png 此接口获取网页截图
splash_url2 = 'http://192.168.43.188:8050/render.png?url={}&wait=3'

#  execute 最强大的接口，此接口可以和splash lua脚本对接
# lua_source={}  lua 代码
splash_url3 = 'http://192.168.43.188:8050/execute?lua_source={}'


def spider(url):
    res = requests.get(splash_url.format(url), headers={'User-Agent': UserAgent().random})
    return res.content.decode("utf-8")

def spider2(url):
    res = requests.get(splash_url2.format(url), headers={'User-Agent': UserAgent().random})
    with open('tt.png', 'wb') as f:
        f.write(res.content)

def spider3(url):
    # lua 代码
    lua_script = '''
        function main(splash)
            splash:go("https://www.guazi.com/bj/buy/")
            splash:wait(2)
            return splash:html()
        end
        '''
    print(splash_url3.format(lua_script))
    res = requests.get(splash_url3.format(quote(lua_script)), headers={'User-Agent': UserAgent().random})
    return res.content.decode("utf-8")

if __name__ == '__main__':
    url = 'https://www.guazi.com/bj/buy/'
    tt = spider3(url)
    print(tt)

