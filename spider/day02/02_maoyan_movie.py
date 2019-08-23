from urllib import request
from urllib import parse
from spider.user_agent import ua_list as u
import re
import time
import random
import csv


class MaoYanSpider(object):
    """
    :param爬取 猫眼电影 Top100榜 数据
    """

    # 初始化
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        self.number = 0

    # 获取响应数据
    def __get_html(self, url):
        headers = {'User-Agent': random.choice(u)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        # 调用提取数据函数
        self.__parse_html(html)

    # 提取需要数据
    def __parse_html(self, html):
        re_pattern = r'<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_pattern, re.S)
        data_list = pattern.findall(html)
        # 调用保存写入函数
        self.__write_html(data_list)

    # 保存写入数据
    def __write_html(self, data_list):
        data_dict = {}
        with open('film.csv', 'a+', encoding='utf-8') as obj:
            for data in data_list:
                data_dict['name'] = data[0].strip()
                data_dict['star'] = data[1].strip()
                data_dict['time'] = data[2].strip()
                self.number += 1


    # 主函数  启动程序
    def main(self):
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.__get_html(url)
            time.sleep(random.randint(1, 3))
        print('共抓取数据： {}条'.format(self.number))

if __name__ == "__main__":
    start_time = time.time()
    spider = MaoYanSpider()
    spider.main()
    end_time = time.time()
    print('总共执行了：%0.2f秒时间'%(end_time - start_time))

