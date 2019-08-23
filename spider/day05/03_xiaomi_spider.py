import requests
import random
import time
from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
from lxml import etree


class XiaoMiSoider(object):

    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.q = Queue()
        self.ua = UserAgent()
        self.count = 0
        self.id_list = []

    def __get_categoryId(self):
        url = 'http://app.mi.com/'
        headers = {'User-Agent': self.ua.random}
        html = requests.get(url=url, headers=headers).text
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath('//ul[@class="category-list"]/li')

        for r in r_list:
            typ_name = r.xpath('./a/text()')[0]
            typ_id = r.xpath('./a/@href')[0].split("/")[-1]
            # 获取每个类型的页数
            pages = self.__get_pages(typ_id)
            self.id_list.append((typ_id, pages))

        self.__putin_url()

    def __get_pages(self, typ_id):
        url = self.url.format(0, typ_id)
        headers = {'User-Agent': self.ua.random}
        html = requests.get(url=url, headers=headers).json()
        count = html['count']
        pages = int(count) // 30 + 1

        return pages

    def __putin_url(self):
        for id in self.id_list:
            for page in range(id[1]):
                url = self.url.format(page, id[0])
                print(url)
                self.q.put(url)

    def __get_data(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                headers = {"User-Agent": self.ua.random}
                html = requests.get(url=url, headers=headers).json()
                self.__parse_html(html)
            else:
                break

    def __parse_html(self, html):
        for app in html['data']:
            name = app['displayName']
            # link =
            print(name)
            self.count += 1
            # time.sleep(random.uniform(1, 2))

    def main(self):
        self.__get_categoryId()
        t_list = []
        for i in range(5):
            t = Thread(target=self.__get_data)
            t_list.append(t)
            t.start()

        for j in t_list:
            j.join()

        print('数量：', self.count)


if __name__ == "__main__":
    start = time.time()
    spider = XiaoMiSoider()
    spider.main()
    end = time.time()
    print('执行了%.2fs时间' % (end - start))
