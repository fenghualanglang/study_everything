from scrapy.cmdline import execute

import sys

import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'douban'])

# redis-cli.exe -h 127.0.0.1 -p 6379
# auth 1qaz2wsx
# lpush douban:start_urls https://movie.douban.com/top250