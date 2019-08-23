import requests
import time
import random
from hashlib import md5

class YdSpider(object):
  def __init__(self):
    # url一定为F12抓到的 headers -> General -> Request URL
    self.url = 'http://fanyi.youdao.com/translate_o?' \
               'smartresult=dict&smartresult=rule'
    self.headers = {
      "Accept": "application/json, text/javascript, */*; q=0.01",
      # "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
      "Content-Length": "237",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Cookie": "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872",
      "Host": "fanyi.youdao.com",
      "Origin": "http://fanyi.youdao.com",
      "Proxy-Connection": "keep-alive",
      "Referer": "http://fanyi.youdao.com/",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest",
    }

  # 获取salt,sign,ts
  def get_salt_sign_ts(self,word):
    pass

  # 主函数
  def attack_yd(self,word):
    # 1. 先拿到salt,sign,ts
    # 2. 定义form表单数据为字典: data={}
    # 3. 直接发请求:requests.post(url,data=data,headers=xxx)
    # 4. 获取响应内容
    pass

  # 主函数
  def main(self):
    # 输入翻译单词
    pass

if __name__ == '__main__':
  spider = YdSpider()
  spider.main()

















