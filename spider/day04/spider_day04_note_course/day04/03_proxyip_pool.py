import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class GetProxyIP(object):
  def __init__(self):
    self.url = 'https://www.xicidaili.com/nn/{}'
    # self.proxies = {
    #   'http': 'http://60.13.42.239:9999',
    #   'https': 'https://60.13.42.239:9999'
    # }

  # 随机生成1个User-Agent
  def get_random_ua(self):
    ua = UserAgent()
    useragent = ua.random

    return useragent

  # 获取可用代理IP文件
  def get_ip_file(self,url):
    headers = {'User-Agent':self.get_random_ua()}
    html = requests.get(url=url,headers=headers,timeout=5).text


    parse_html = etree.HTML(html)
    tr_list = parse_html.xpath('//tr')
    for tr in tr_list[1:]:
      ip = tr.xpath('./td[2]/text()')[0]
      port = tr.xpath('./td[3]/text()')[0]
      # 测试ip:port是否可用
      self.test_ip(ip,port)

  def test_ip(self,ip,port):
    proxies = {
      'http':'http://{}:{}'.format(ip,port),
      'https': 'https://{}:{}'.format(ip, port),
    }
    test_url = 'http://www.baidu.com/'
    try:
      res = requests.get(url = test_url,proxies = proxies,timeout = 8)
      if res.status_code == 200:
        print(ip,port,'Success')
        with open('proxies.txt','a') as f:
          f.write(ip + ':' + port + '\n')
    except Exception as e:
      print(ip,port,'Failed')

  # 主函数
  def main(self):
    for i in range(1,1001):
      url = self.url.format(i)
      self.get_ip_file(url)
      time.sleep(random.randint(0,1))

if __name__ == '__main__':
  spider = GetProxyIP()
  spider.main()


















