from urllib import request
import re
import time
import random
from useragents import ua_list
import pymysql

class MaoyanSpider(object):
  def __init__(self):
    self.url = 'https://maoyan.com/board/4?offset={}'
    # 计数
    self.num = 0
    # 创建2个对象
    self.db = pymysql.connect(
      'localhost','root','123456','maoyandb',charset='utf8'
    )
    self.cursor = self.db.cursor()

  def get_html(self,url):
    headers = {
      'User-Agent' : random.choice(ua_list)
    }
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 直接调用解析函数
    self.parse_html(html)

  def parse_html(self,html):
    re_bds = r'<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
    pattern = re.compile(re_bds,re.S)
    # film_list: [('霸王别姬','张国荣','1993'),()]
    film_list = pattern.findall(html)
    # 直接调用写入函数
    self.write_html(film_list)

  # # mysql - execute()
  # def write_html(self,film_list):
  #   ins = 'insert into filmtab values(%s,%s,%s)'
  #   for film in film_list:
  #     L = [
  #       film[0].strip(),
  #       film[1].strip(),
  #       film[2].strip()[5:15]
  #     ]
  #     self.cursor.execute(ins,L)
  #     # 千万别忘了提交到数据库执行
  #     self.db.commit()

    # mysql - executemany([(),(),()])
  def write_html(self, film_list):
    L = []
    ins = 'insert into filmtab values(%s,%s,%s)'
    for film in film_list:
      t = (
        film[0].strip(),
        film[1].strip(),
        film[2].strip()[5:15]
      )
      L.append(t)

    self.cursor.executemany(ins, L)
    # 千万别忘了提交到数据库执行
    self.db.commit()

  def main(self):
    for offset in range(0,31,10):
      url = self.url.format(offset)
      self.get_html(url)
      time.sleep(random.randint(1,2))

    # 断开数据库连接
    self.cursor.close()
    self.db.close()

if __name__ == '__main__':
  start = time.time()
  spider = MaoyanSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))






















