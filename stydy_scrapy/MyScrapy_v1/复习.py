
1 反爬措施
    1.1 服务器端为什么要做反爬
        1.降低负载
        2.保护数据
    1.2 反爬的几个方向，举例
        1.识别用户身份
            User-agent
            cookies
            referer
            验证码
                登录验证码
                频繁访问验证码

                手动输入
                图片识别引擎
                打码平台
            ...
        2.分析用户行为
            并发量
                ip
                cookies
            在线时间
                设置休眠
                    time.sleep(random.randint(3600*24)
            蜜罐
                设置一些正常用户不会点击的链接，但是爬虫会按照指定的规则提取，并且访问，一旦访问，IP地址暴露被封
        3.动态数据加载
            ajax    抓包
            js

2 scrapy反反爬与下载器中间件
    2.1 设置user-agent的方式，优先级
        settings
            USER-AGENT= ''
            DEFAULT_REQUEST_HEADERS={

            }
        创建请求的时候
            Request(url,callback,headers)
        下载器中间件
            中间件类
                process_requests(self,Request，spider)

    2.2 如何设置请求延迟,效果
        settings
            DOWNLOAD_DELAY = 3

    2.3 如何设置不带cookies请求
        COOKIES_ENABLED = False

    2.4 ip代理池
        IP代理商
            收费
            免费
        自行搭建
            云服务器
            vps
            ADSL拨号服务器
        crawlera

    2.5 下载器中间的功能
        全局修改请求与响应

    2.6 下载器中间的编写方法
        middlerwares文件中编写
            定义中间件类
                process_request()
        settings文件中注册

3 手机抓包
    设置pc 开启wifi 获取IP地址
    设置手机    链接wifi 高级设置中设置代理(将开wifi的电脑IP地址设置为服务器，port为8888)

    操作手机app产生流量

4.图片管道
    发送请求，在完成的方法中获取图片下载信息
