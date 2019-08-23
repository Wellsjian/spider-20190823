import requests
from lxml import etree
import random
from useragents import ua_list
import os

class CodeSpider(object):
  def __init__(self):
    self.url = 'http://code.tarena.com.cn' \
               '/AIDCode/aid1904/14-redis/'
    self.auth = ('tarenacode','code_2013')

  def parse_html(self):
    # 获取响应内容
    html = requests.get(
      url = self.url,
      headers = {'User-Agent':random.choice(ua_list)},
      auth = self.auth
    ).content.decode('utf-8','ignore')

    # 解析
    parse_html = etree.HTML(html)
    # r_list: ['../','day01/','redis-xxx.zip']
    r_list = parse_html.xpath('//a/@href')
    for r in r_list:
      if r.endswith('.zip') or r.endswith('.rar'):
        self.save_files(r)

  def save_files(self,r):
    # 操作目录 /home/tarena/redis/
    directory = '/home/tarena/AID/redis/'
    # 一定记住
    if not os.path.exists(directory):
      os.makedirs(directory)

    # 拼接地址,把zip文件保存到指定目录
    url = self.url + r
    # filename: /home/tarena/AID/redis/xxx.zip
    filename = directory + r
    html = requests.get(
      url = url,
      headers = {'User-Agent':random.choice(ua_list)},
      auth = self.auth
    ).content

    with open(filename,'wb') as f:
      f.write(html)
      print('%s下载成功' % r)


if __name__ == '__main__':
  spider = CodeSpider()
  spider.parse_html()
















