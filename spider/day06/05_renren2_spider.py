import requests
from lxml import etree


class RenRenSpder(object):

    def __init__(self):
        #表单移交地址
        self.__post_url = "http://www.renren.com/PLogin.do"
        #个人主页地址
        self.__get_url = "http://www.renren.com/967469305/profile"
        #实例化 session对象
        self.session = requests.session()

    def get_html(self):
        form_data = {
            "email":'15110225726',
            'password':'zhanshen001'
        }
        #先session post
        self.session.post(url=self.__post_url, data=form_data)
        html = self.session.get(url=self.__get_url).text
        # print(html)
        self.parse_html(html)

    def parse_html(self, html):
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath('//li[@class="school"]/span/text()')
        print(r_list)

if __name__ =='__main__':
    spider = RenRenSpder()
    spider.get_html()

