import requests
import csv
import time
import re
import random
from user_agent import ua_list as u


class HouseSpider(object):

    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}'

    # 1.获取HTML；
    def __get_html(self, url):
        headers = {'User-Agent': random.choice(u)}
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        self.__parse_html(html)

    # 2.提取数据
    def __parse_html(self, html):
        re_bds = r'<div class="title">.*?data-sl="">(.*?)</a>.*?class="totalPrice">.*?<span>(.*?)</span>.*?class="unitPrice".*?<span>(.*?)</span>'
        pattern = re.compile(re_bds, re.S)
        data_list = pattern.findall(html)
        self.__write_html(data_list)

    # 写入csv文件
    def __write_html(self, data_list):
        if data_list:
            with open('lianjia.csv', 'a', encoding='utf-8', newline="") as obj:
                writer = csv.writer(obj)
                list01 = []
                for data in data_list:
                    tuple01 = (
                        data[0].strip(),
                        data[1].strip()+'万',
                        data[2].strip(),
                    )
                    list01.append(tuple01)
                writer.writerows(list01)
        else:
            print('匹配为空')

    # 4启动服务
    def main(self):
        for page in range(1, 101):
            url = self.url.format(page)
            self.__get_html(url)
            time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    spider = HouseSpider()
    spider.main()
