# -*- coding: utf-8 -*-
import hashlib
import json
import random
import time

import scrapy

from day10.Youdao.Youdao.items import YoudaoItem


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']

    word = input("请输入查询单词:")
    def start_requests(self):
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        salt, ts, sign = self.get_sign_salt_ts_bv(word=self.word)
        form_data = {
            "i": self.word,
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
        # cookies = self.get_cookies()
        yield scrapy.FormRequest(
            url=post_url,
            formdata = form_data,
            callback=self.parse_html
        )

    def parse_html(self, response):
        item = YoudaoItem()
        html = json.loads(response.text)
        # print(html)
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item

    def  get_sign_salt_ts_bv(self, word):
        ts = str(int(time.time()*1000))
        s = hashlib.md5()
        salt = ts + str(random.randint(0,9))
        s.update(("fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj").encode())
        sign = s.hexdigest()
        return salt, ts, sign


