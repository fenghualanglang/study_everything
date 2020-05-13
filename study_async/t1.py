
import requests
from lxml import etree
from model import CodePost

class India():

    def __init__(self):

        self.headers = {
            "Referer": "https://ind.youbianku.com/zh-hans/state/Uttar_Pradesh?page=2",
            "Sec-Fetch-Dest": "document",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }
        self.base_url = 'https://ind.youbianku.com'

    def parse_zhou_url(self, url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.content.decode('utf8'))
        zhou_list = html.xpath('//*[@id="node-15217"]/div/div/div/div/fieldset[1]/div/div/table/tbody/tr/td/a/@href')
        return zhou_list

    def parse_quhua1_url(self, zhou_url):
        url = self.base_url + zhou_url
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.content.decode('utf8'))
        quhua1_url_list = html.xpath('//*[@class="views-field views-field-field-admin2"]/a/@href')
        return quhua1_url_list

    def parse_quhua2_url(self, quhua1_url):
        url = self.base_url + quhua1_url
        print(url)
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.content.decode('utf8'))
        quhua2_list = html.xpath('//tbody/tr[position()>1]')
        for iquhua2 in quhua2_list:
            one_addr = html.xpath('//span[@itemprop="addressLocality"]/a/text()')[0]
            tow_addr = iquhua2.xpath('td[1]/text()')[0]
            thr_addr = iquhua2.xpath('td[2]/text()')[0]
            code = iquhua2.xpath('td[3]/a/text()')[0]
            CodePost.create(
                one_addr=one_addr,
                tow_addr=tow_addr,
                thr_addr=thr_addr,
                code=code
            )

    def run(self):
        url = 'https://ind.youbianku.com/zh-hans'
        zhou_url_list = self.parse_zhou_url(url)
        for zhou_url in zhou_url_list:
            quhua1_url_list = self.parse_quhua1_url(zhou_url)
            for quhua1_url in quhua1_url_list:
                self.parse_quhua2_url(quhua1_url)
# 你咋不上天呢
# 本小仙女就是从天上来的



if __name__ == '__main__':
    india = India()
    india.run()