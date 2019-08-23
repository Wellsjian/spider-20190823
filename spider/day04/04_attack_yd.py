import hashlib
import requests
from lxml import etree
import random
import time


class YdSpider(object):

    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "238",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1039448775@43.254.90.134; JSESSIONID=abcpq_8STuptCh8nuikYw; OUTFOX_SEARCH_USER_ID_NCOO=413106244.4840502; ___rl__test__cookies=1565686670659",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        # self.headers = {
        #     "Cookie": "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872",
        #     "Referer": "http://fanyi.youdao.com/",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        # }


    def __get_salt_sign_ts(self, word):
        # t = n.md5(navigator.appVersion)
        # r = "" + (new Date).getTime()
        # i = r + parseInt(10 * Math.random(), 10);
        # ts: r,
        # bv: t,
        # salt: i,
        # sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
        # ts = str(int(time.time() * 1000))
        # salt = ts + str(random.randint(0, 9))
        # string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        # s = hashlib.md5()
        # s.update(string.encode())
        # sign = s.hexdigest()
        # return salt, ts, sign
        # salt
        salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = hashlib.md5()
        s.update(string.encode())
        sign = s.hexdigest()
        # ts
        ts = str(int(time.time() * 1000))
        return salt, ts, sign

    def __attack_yd(self, word):
        # 1. 先拿到 salt, ts , sign
        salt, ts, sign = self.__get_salt_sign_ts(word)
        # 2. 定义form表单数据为字典  data={}
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'cf156b581152bd0b259b90070b1120e6',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        # 3. 直接发请求， request.post(url, headers, data)
        res = requests.post(
            url=self.url,
            data=data,
            headers=self.headers
        )
        # html = res.text
        # with open('youdao.html', 'w') as obj:
        #     obj.write(html)
        # if res.content:
        html = res.json()
        print(html)
        print(type(html))
        print(html['translateResult'][0][0]['src'])
        # json_html = requests.post(self.url, data=data, headers=self.headers).json()
        # result = json_html['translateResult'][0][0]['tgt']
        # print(result)
        # 4. 获取响应内容.

    def main(self):
        word = input("请输入翻译单词：")
        self.__attack_yd(word)


if __name__ == "__main__":
    spider = YdSpider()
    spider.main()
