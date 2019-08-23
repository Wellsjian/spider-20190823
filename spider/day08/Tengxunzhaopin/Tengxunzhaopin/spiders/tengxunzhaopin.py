# -*- coding: utf-8 -*-
import scrapy
import json


class TengxunzhaopinSpider(scrapy.Spider):
    name = 'tengxunzhaopin'
    allowed_domains = ['careers.tencent.com/']

    def start_requests(self):
        for job in range(40001,40012):
            url = 'https://careers.tencent.com/search.html?pcid={}'.format(str(job))
            yield scrapy.Request(
                url=url,
                callback=self.first_parse_html
            )
    def first_parse_html(self, response):
        for index in range(1, 226):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566218228586&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=gb'.format(str(index))
            print('*'*50)
            yield scrapy.Request(
                url=url,
                callback=self.second_parse_html
            )

    def second_parse_html(self, response):
        print(response.text)

