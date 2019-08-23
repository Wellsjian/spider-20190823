import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class ProxyIp(object):

    def __init__(self):
        # self.url = 'http://www.89ip.cn/index_{}.html'
        # self.url = 'https://www.kuaidaili.com/free/inha/{}'
        self.url = 'http://www.xiladaili.com/gaoni/{}'

    def __get_user_agent(self):
        ua = UserAgent()
        user_agent = ua.random
        return user_agent

    def __get_ip_html(self, url):
        headers = {'User-Agent': self.__get_user_agent()}
        # print(headers)
        # proxies = {
        #     'http': 'http://111.77.22.219:9000',
        #     'https': '111.77.22.219:9000'
        # }
        # print(222)
        res = requests.get(url=url, headers=headers)

        # print(res)
        html = res.content.decode('utf-8', 'ignore')
        # print(html)
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr')

        for tr in tr_list[1:]:
            res = tr.xpath('./td[1]/text()')[0].strip().split(':')
            ip = res[0]
            # print(ip)
            port = res[1]
            print(ip, port)
            time.sleep(random.uniform(5, 8))
            self.__test_ip(ip, port)

    def __test_ip(self, ip, port):
        proxies = {
            'http': 'http://{}：{}'.format(ip, port),
            'https': 'https://{}：{}'.format(ip, port)
        }
        url = 'http://www.baidu.com'
        print(proxies)
        try:
            res = requests.get(
                url=url,
                proxies=proxies,
                timeout=5
            )

            if res.status_code == 200:
                print(ip, port, '123465')
                time.sleep(random.uniform(2, 3))
                with open('proxies.txt', 'a') as obj:
                    obj.write('{}:{}'.format(ip, port) + '\n')
        except Exception as e:
            print(e, 'failed')

    def main(self):
        for page in range(1, 1000):
            url = self.url.format(page)
            print(url)
            self.__get_ip_html(url)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    spider = ProxyIp()
    spider.main()
