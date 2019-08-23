import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class ProxyIp(object):

    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/{}'
        # self.url = 'https://www.kuaidaili.com/free/inha/{}'

    def __get_user_agent(self):
        ua = UserAgent()
        user_agent = ua.random
        return user_agent

    def __get_ip_html(self, url):
        headers = {'User-Agent': self.__get_user_agent()}
        res = requests.get(url=url, headers=headers)
        html = res.content.decode('utf-8', 'ignore')
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr')
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[2]/text()')[0].strip()
            port = tr.xpath('./td[3]/text()')[0].strip()
            self.__test_ip(ip, port)

    def __test_ip(self, ip, port):
#         proxies = {
#             'http': 'http://{}：{}'.format(ip, port),
#             'https': 'https://{}：{}'.format(ip, port)
#         }
#         test_url = 'http://www.baidu.com/'
#         try:
#             res = requests.get(url=test_url, proxies=proxies)
#             if res.status_code == 200:
#                 print(ip, port, '123465')
#                 with open('proxies.txt', 'a') as obj:
#                     obj.write('{}:{}'.format(ip, port) + '\n')
#
#         except Exception as e:
#             print(ip, port, 'failed')
# #
        proxies = {
            'http': 'http://{}:{}'.format(ip, port),
            'https': 'https://{}:{}'.format(ip, port),
        }
        test_url = 'http://www.baidu.com/'
        try:
            res = requests.get(url=test_url, proxies=proxies, timeout=8)
            if res.status_code == 200:
                print(ip, port, 'Success')
                with open('proxies.txt', 'a') as f:
                    f.write(ip + ':' + port + '\n')
        except Exception as e:
            print(ip, port, 'Failed')

    def main(self):
        for page in range(1, 1000):
            url = self.url.format(page)
            self.__get_ip_html(url)



if __name__ == "__main__":
    spider = ProxyIp()
    spider.main()
