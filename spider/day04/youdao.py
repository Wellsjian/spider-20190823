import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class ProxyIp(object):

    def __init__(self):
        # self.url = 'http://www.89ip.cn/index_{}.html'
        self.url = 'https://www.xicidaili.com/nn/{}'

    def __get_user_agent(self):
        ua = UserAgent()
        user_agent = ua.random
        return user_agent

    def __get_ip_html(self, url):
        headers = {'User-Agent': self.__get_user_agent()}
        print(headers)
        proxies = {
            'http': 'http://60.13.42.180:9999',
            'https': 'https://60.13.42.180:9999'
        }
        res = requests.get(url=url, headers=headers, proxies=proxies)
        html = res.content.decode('utf-8', 'ignore')
        print(html)
        with open('456.html', 'w') as f:
            f.write(html)

    def main(self):
        for num in range(1,10):
            url = self.url.format(num)
            self.__get_ip_html(url)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    spider = ProxyIp()
    spider.main()
