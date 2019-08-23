import random
import requests
import time
from lxml import etree
import json
from fake_useragent import UserAgent


class DouBanSpider(object):

    def __init__(self):
        self.base_url = 'https://movie.douban.com/j/chart/top_list?'
        self.count = 0
    def __get_html(self, params):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        html = requests.get(url=self.base_url, params=params, headers=headers).json()
        self.__parse_html(html)

    def __parse_html(self, html):
        # html [{}, {}, {}]
        item = {}
        for i in html:
            item['title'] = i['title']
            item['score'] = i['score']
            item['actors'] = i['actors']
            self.count += 1
            print(item)
            time.sleep(random.randint(1,2))
    #获取电影总数
    def __get_total(self, type):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type)
        html = requests.get(url=url, headers=headers).json()
        return html['total']

    def main(self):

        typ = input('请输入电影类型(剧情|动作|喜剧)')
        type_dict = {"剧情":'11', '动作':'5', '喜剧':'24'}
        type = type_dict[typ]
        total = self.__get_total(type)
        print(total)
        for page in range(0, int(total), 20):
            params = {
                'type': type,
                'interval_id': '100:90',
                'action':'',
                'start': '{}'.format(page),
                'limit': '20'
            }
            self.__get_html(params=params)
            time.sleep(random.uniform(1,2))
        print('共抓取{}'.format(self.count))
        print(total)
if __name__ == "__main__":
    spider = DouBanSpider()
    spider.main()
