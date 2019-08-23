import requests
from lxml import etree
import re
import pymysql

class GovermentSpider(object):

    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password ='123456',
            database='govement',
            charset='utf8'
        )
        self.cur = self.db.cursor()
    def  get_false_html(self):
        html = requests.get(url=self.url, headers=self.headers).text
        parse_html = etree.HTML(html)

        r_list = parse_html.xpath('//a[@class="artitlelist"]')
        false_link = ''
        for r in r_list:
            # title = r.xpath('')
            title = r.get('title')
            if title.endswith('代码'):
                false_link += 'http://www.mca.gov.cn' + r.get('href')

                break

        self.increment_spider(false_link)

    def increment_spider(self, false_link):
        sql = 'select url from url_info where url=%s'
        self.cur.execute(sql, [false_link])
        result = self.cur.fetchall()
        if not result:
            self.get_true_link(false_link)
            sql = 'insert into url_info (url) values (%s)'
            self.cur.execute(sql, [false_link])
            self.db.commit()
        else:
            print('该数据已存在')

    def get_true_link(self, false_link):
        html = requests.get(url=false_link, headers=self.headers).text
        #利用正则提出真链接
        pattern = re.compile(r'window.location.href="(.*?)"', re.S)
        true_link = pattern.findall(html)[0]
        # with open('goverment.html', 'w') as f:
        #     f.write(html)
        print(true_link)
        self.save_data(true_link)

    def save_data(self, true_link):
        html = requests.get(url=true_link, headers=self.headers).text

        parse_html = etree.HTML(html)

        r_list = parse_html.xpath('//tr[@height="19"]')
        print(r_list)

        for r in r_list:
            code = r.xpath('./td[2]/text()')[0].strip()
            name = r.xpath('./td[3]/text()')[0].strip()
            print(code, name)


    def main(self):
        self.get_false_html()


if __name__ == "__main__":
    spider = GovermentSpider()
    spider.main()













