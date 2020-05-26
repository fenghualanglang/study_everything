# -*- coding: utf-8 -*-

# Scrapy settings for MyScrapy project

BOT_NAME = 'MyScrapy'

SPIDER_MODULES = ['MyScrapy.spiders']
NEWSPIDER_MODULE = 'MyScrapy.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'MyScrapy.middlewares.MyscrapyDownloaderMiddleware': 543,
    # 自定义ua池
    'MyScrapy.middlewares.UserAgentMilldewares': 544,

    # 在其中集成selenium
    # 'MyScrapy.middlewares.SeliniumMilldewares': 544,

    # 在其中集成代理池
    # 'MyScrapy.middlewares.RandomProxy': 545,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'MyScrapy.pipelines.MyscrapyWritePipeline': 300,
    # 'MyScrapy.pipelines.MyscrapyPipeline': 301,

    # 自定义ImagesPipeline
    # 'MyScrapy.pipelines.ImagePipeline': 302,

    # 引入Scrapy提供的ImagesPipeline组件
    # 'scrapy.pipelines.images.ImagesPipeline': 303,

    # 'MyScrapy.pipelines.MySQLPipeline': 304,

    # 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item
    'MyScrapy.pipelines.DoubanPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400

}

# 使用了scrapy_redis的去重组件，在redis数据库里做去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy_redis的调度器，在redis里分配请求
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复
SCHEDULER_PERSIST = True


# 如果不启用则按scrapy默认的策略
#  默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#  可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
#  可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'


# redis数据库的连接参数
REDIS_HOST = '192.168.43.188'
REDIS_PORT = 6379
REDIS_USER = 'root'
REDIS_PARAMS = {'password': '1qaz2wsx'}

# 配置日志路径
# LOG_FILE = './log'  #文件路径
LOG_LEVEL = 'DEBUG'

MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'douban'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1qaz2wsx'


# 自己构建代理池
PROXY_LIST = [
    {"IP":"42.242.36.37","Port":'40472'},
    {"IP":"121.232.154.13","Port":'40266'}
]

# 自构建UA池
USER_AGENT_LIST =[
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HCI0449; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; i-NavFourF; .NET CLR 1.1.4322) "
]
