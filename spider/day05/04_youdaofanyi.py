import requests
import random
import time
import hashlib

class YouDaoSpider:

    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "251",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1039448775@43.254.90.134; OUTFOX_SEARCH_USER_ID_NCOO=413106244.4840502; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcsA-TscoFtl8oyd5pYw; ___rl__test__cookies=1565782252253",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
#     t = n.md5(navigator.appVersion)
#     r = "" + (new Date).getTime()
#     i = r + parseInt(10 * Math.random(), 10);
#     ts: r,
#     bv: t,
#     salt: i,
#     sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")

    def  __get_sign_salt_ts_bv(self, word):
        ts = str(int(time.time()*1000))
        print(ts)
        s = hashlib.md5()
        salt = ts + str(random.randint(0,9))
        s.update(("fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj").encode())
        sign = s.hexdigest()
        return salt, ts, sign
        # print(sign)
        # salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
        # # sign
        # string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        # s = hashlib.md5()
        # s.update(string.encode())
        # sign = s.hexdigest()
        # # ts
        # ts = str(int(time.time() * 1000))

        # return ts, salt, sign

    def __get_html(self, word):
        salt, ts, sign = self.__get_sign_salt_ts_bv(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": '65313ac0ff6808a532a1d4971304070e',
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        json_html = requests.post(url=self.url, data=data, headers=self.headers).json()
        print(json_html['translateResult'][0][0]['tgt'])


    def main(self):
        word = input("请输入查询单词：")
        self.__get_html(word)


if __name__ == "__main__":
    spider = YouDaoSpider()
    spider.main()





