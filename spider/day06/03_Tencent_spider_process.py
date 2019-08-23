import requests
import json
from lxml import etree
from fake_useragent import UserAgent
from multiprocessing import Process
from queue import Queue
import time
import random


class TencentSpider(object):

    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1565834647827&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=gb'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1565834860777&postId={}&language=zh-cn'
        self.count = 0
        self.q = Queue()
        self.list01 = []
        self.f = open('xiaomi2.json', 'a')

    def __put_in_queue(self):
        pages = self.__get_page()
        for page in range(1, 3):
            url = self.one_url.format(page)
            print(url)
            self.q.put(url)

    # 创建线程
    def __create_thread(self, func):
        t_list = []
        for i in range(20):
            t = Process(target=func)
            t_list.append(t)
            t.start()

        for j in t_list:
            j.join()

    def __get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        html = json.loads(html)
        return html

    def __parse_html(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                html = self.__get_html(url)
                item = {}

                for data in html['Data']['Posts']:
                    item['name'] = data['RecruitPostName']
                    postId = data['PostId']
                    html = self.__get_html(self.two_url.format(postId))
                    item['工作职责'] = html['Data']['Responsibility'].replace('\r\n', ' ').replace('\n', ' ')
                    item['工作要求'] = html['Data']['Requirement'].replace('\r\n', ' ').replace('\n', ' ')
                    print(item)
                    self.count += 1
                    self.list01.append(item)
                json.dump(self.list01, self.f, ensure_ascii=False)
            else:
                self.f.close()
                break

    def __get_page(self):
        url = self.one_url.format(1)
        html = self.__get_html(url)
        count = html['Data']['Count']
        pages = int(count) // 10 + 1
        return pages

    def main(self):
        self.__put_in_queue()
        self.__create_thread(self.__parse_html)



        print('数量', self.count)


if __name__ == "__main__":
    spider = TencentSpider()
    spider.main()
