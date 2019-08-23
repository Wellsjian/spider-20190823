# -*- coding: utf-8 -*-
import json

import scrapy

from day09.So.So.items import SoItem


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com/']

    def start_requests(self):
        for page in range(5):
            url = 'http://image.so.com/zjl?ch=beauty&direction=next&sn={}&pn=30&prevsn=-1'.format(str(page*30))
            # 把url地址入队列
            yield scrapy.Request(
                url = url,
                callback = self.parse_img
            )

    def parse_img(self, response):
        html = json.loads(response.text)

        for img in html['list']:
            item = SoItem()
            # 图片链接
            item['img_url'] = img['qhimg_url']
            item['img_title'] = img['title']
            yield item
