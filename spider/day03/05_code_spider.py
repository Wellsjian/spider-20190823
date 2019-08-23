import random
import requests
import time
from user_agent import ua_list as u
from lxml import etree
import os


class CodeSpider(object):

    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1904/15-spider/'
        self.auth = ('tarenacode', 'code_2013')

    def __get_html(self, url):
        headers = {
            "User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

        res = requests.get(url=url, auth=self.auth, headers=headers)
        # res.encoding = "gbk"
        # html = res.content.decode('utf-8', 'ignore')
        # print(html)
        html = res.content
        return html

    def __xpath_html(self, html):
        params_html = etree.HTML(html)
        r_list = params_html.xpath('//a/@href')
        # print(r_list)
        return r_list

    def __parse_html(self):
        html = self.__get_html(self.url)
        r_list = self.__xpath_html(html)
        for r in r_list:
            if r.endswith('.zip'):
                self.__download_html(r)
                time.sleep(random.randint(1,2))
    def __download_html(self, r):
        # html = requests.get(
        #     url=self.url + r,
        #     headers = {'User-Agent':random.choice(u)},
        #     auth = self.auth
        # ).content
        url = self.url + r
        html = self.__get_html(url)
        path = '/home/tarena/materials/xiaojian/forth_phase/spider/day03/notecode/'
        if not os.path.exists(path):
            os.makedirs(path)
        filename = path  + r
        with open(filename, 'wb') as obj:
            obj.write(html)
            print('%s 下载成功'% filename)




    def main(self):

        self.__parse_html()


if __name__ == "__main__":
    spider = CodeSpider()
    spider.main()







