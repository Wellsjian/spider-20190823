from urllib import request
from urllib import parse

import pymysql

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
        #连接数据库
        self.db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='maoyan',
            charset='utf8'
            )
        self.cursor = self.db.cursor()

    #将数据写入数据库中   excutemany   [(),(),(),()]   excute   []
    def write_database(self, data_list):
        try:
            sql = 'insert into data values(%s,%s,%s)'
            self.cursor.executemany(sql,dat  a_list)
            self.db.commit()
        except Exception as e:
            print('Error is', e)
            self.db.rollback()

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
        if data_list:
            list01 = []
            for data in data_list:
                tuple01 = (
                    data[0].strip(),
                    data[1].strip()[3:15],
                    data[2].strip()[5:15],
                )
                list01.append(tuple01)
                self.number += 1
            self.write_database(list01)

    # 主函数  启动程序
    def main(self):
        for offset in range(0, 31, 10):
            url = self.url.format(offset)
            self.__get_html(url)
            time.sleep(random.randint(1, 3))
        print('共抓取数据： {}条'.format(self.number))

        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    start_time = time.time()
    spider = MaoYanSpider()
    spider.main()
    end_time = time.time()
    print('总共执行了：%0.2f秒时间' % (end_time - start_time))
