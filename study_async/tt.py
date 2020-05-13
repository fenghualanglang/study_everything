import requests
from lxml import etree

from model import PostCode

class India():

    def __init__(self):

        self.base_url = 'https://www.nowmsg.com/findzip/county.asp?'
        self.headers = {
            "referer": "https://www.nowmsg.com/findzip/county.asp?country=IN&state=Andaman%20%26%20Nicobar%20Islands",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        }


    def administrative_area(self, url):
        response = requests.get(url)
        return etree.HTML(response.text)

    def parse_area_url(self, html):
        area_list = html.xpath('/html/body/div[2]/div/div[2]/div[5]/div/div/a/text()')
        return area_list

    # 辖区县 / 郡的邮编
    def parse_state_list(self, area):
        params = {
            "country": "IN",
            "state": area
        }
        response = requests.get(url=self.base_url, params=params)
        html = etree.HTML(response.text)
        state_list = html.xpath('/html/body/div[3]/div/div/a/text()')
        return state_list

    # county 的邮编
    def parse_county_list(self, area, state):

        params = {
            "country": "IN",
            "state": area,
            "county": state
        }

        city_url = 'https://www.nowmsg.com/findzip/city.asp?'
        response = requests.get(url=city_url, params=params, headers=self.headers)
        html = etree.HTML(response.content.decode('utf8'))
        county_list = html.xpath('//div[@class="col-md-3 my-padding-6"]/a/text()')
        return county_list

    def parse_city_code(self, area, state, city):
        postal_code_url = 'https://www.nowmsg.com/findzip/postal_code.asp?'
        params = {
            "country": "IN",
            "state": area,
            "county": state,
            "city": city
        }
        response = requests.get(url=postal_code_url, params=params, headers=self.headers)
        '''
        邮编	地名/城市	乡/村/社区	县/郡	州/市	纬度	经度
        '''
        html = etree.HTML(response.content.decode('utf8'))
        # 邮编
        code = html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[1]/text()')[0]
        # 地名/城市
        city = html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[2]/text()')[0]
        # 乡 / 村 / 社区
        township = html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[3]/text()')[0]
        # '县/郡'
        county= html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[4]/text()')[0]
        # 纬度
        latitude = html.xpath('//html/body/div[3]/div/div/table/tbody/tr/td[5]/text()')[0]
        # 经度
        longitude = html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[6]/text()')[0]
        area = html.xpath('/html/body/div[3]/div/div/table/tbody/tr/td[7]/text()')[0]

        print(f'邮编{code}	地名/城市{city}	乡/村/社区{township}	县/郡{county}	州/市{area}	纬度{latitude}	经度{latitude}')

        PostCode.create(
            code=code,
            city=city,
            township=township,
            county=county,
            latitude=latitude,
            longitude=longitude,
            area=area
        )

    def run(self):
        i = 0
        url = 'https://www.nowmsg.com/findzip/in_postal_code.asp'
        area_html = self.administrative_area(url)
        area_list = self.parse_area_url(area_html)
        for area in area_list:
            # print("行政区", area)
            state_list = self.parse_state_list(area)
            for state in state_list:
                # print("辖区县 / 郡的邮编", state)
                county_list = self.parse_county_list(area, state)
                for county in county_list:
                    self.parse_city_code(area, state, county)



if __name__ == '__main__':
    india = India()
    india.run()
