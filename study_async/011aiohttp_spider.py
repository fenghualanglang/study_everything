
import re
import asyncio
import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = 'http://www.jobbole.com/'

stopping = False
waitting_url = []
seen_urls = set()

sem = asyncio.Semaphore(1) #设置并发度

async def fetch(url, session):
    async with sem:
        try:
            async with session.get(url) as resp:
                print(f'url status: {resp.status}')
                if resp.status in [200, 201]:
                    print(await resp.text())
                    return await resp.text()
        except Exception as e:
            print(e)


def extract_urls(html):

    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr("href")
        if url and url.startswith('http') and url not in seen_urls:
            urls.append(url)
            waitting_url.append(url)
    return urls

async def init_urls(url, session):

    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)

async def article_handler(url, session, pool):
    # 获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq('doc_title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = f"insert into article(title) value ({title})"
            await cur.execute(insert_sql)



async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if not len(waitting_url):
                await asyncio.sleep(7)
                continue
            url = waitting_url.pop()
            print(f'start get  url {url}')
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session)

async def main(loop):
    # 创建mysql 链接池
    pool = await aiomysql.create_pool(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='1qaz2wsx',
        db='crm',
        loop=loop,
        charset="utf8",
        autocommit=True
    )

    asyncio.ensure_future(init_urls(start_url))
    asyncio.ensure_future(consumer(pool))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()















