from selenium import webdriver

# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')
print(driver.page_source)

'''
滚动条
#   执行js
js = 'document.documentElement.scrollTop=1000
driver.execute_script(js)



Scrapy Splash 用来爬取动态网页，其效果和scrapy selenium phantomjs一样，
都是通过渲染js得到动态网页然后实现网页解析，selenium+phantomjs是用selenium的Webdriver操作浏览器，
然后用phantomjs执行渲染脚本得到结果，一般再用BeautifulSoup处理。Splash是官推的js渲染引擎，
和Scrapy结合比较好，使用的是webkit开发的轻量级无界面浏览器，渲染之后结果和静态爬取一样可以直接用xpath处理。只是splash是在docker中运行。

'''

