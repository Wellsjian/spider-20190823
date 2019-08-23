# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TengxunzhaopingItem
from urllib import parse
import requests
from scrapy_redis.spiders import RedisSpider


class TengxunzhaopingSpider(RedisSpider):
    name = 'tengxunzhaoping'
    allowed_domains = ['careers.tencent.com/']
    one_url = 'https://careers.tencent.com/search.html?pcid={}'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    user_input = input("请输入类型:")
    page_one_urr = two_url.format(user_input, 1 )
    # start_url = [page_one_url]
     # start_urls = ['http://careers.tencent.com//']
    redis_key = 'tenxunzhaoping:spider'

    def parse(self, response):

        for job in range(40001,40012):
            url = self.one_url.format(job)
            yield scrapy.Request(
                url=url,
                callback=self.parse_first_html
            )

    def get_total_page(self):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566301036883&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40003&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=gb'.format('', 1)
        html = requests.get(url=url).json()
        total = int(html['Data']['Count'] ) // 10 + 1
        return total

    def parse_first_html(self, response):
        #给users_input 进行编码
        user_input = parse.quote(self.user_input)
        total = self.get_total_page()
        for index in range(1, 11):
            url = self.two_url.format(user_input,index)
            yield scrapy.Request(
                url=url,
                dont_filter=True,
                callback=self.parse_second_html
            )

    def parse_second_html(self, response):
        html = response.text
        html = json.loads(html)
        for job in html['Data']['Posts']:
            post_id = job['PostId']
            url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566267859060&postId={}&language=zh-cn'.format(post_id)

            yield scrapy.Request(
                url=url,
                dont_filter=True,
                callback=self.parse_three_html
            )


    def parse_three_html(self, response):
        item = TengxunzhaopingItem()
        html = json.loads(response.text)
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_require'] = html['Data']['Responsibility']
        item['job_address'] = html['Data']['LocationName']
        item['job_time'] = html['Data']['LastUpdateTime']

        yield item

