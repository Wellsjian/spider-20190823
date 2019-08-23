# -*- coding: utf-8 -*-
import json

import scrapy

from day11.Tuniu.Tuniu.items import TuniuItem
from day11.get_dict import src_citys, dst_citys


class TuniuSpider(scrapy.Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']


    def start_requests(self):
        s_city = input('出发城市:')
        d_city = input('相关目的地:')
        start_time = input('出发时间(20190828):')
        end_time = input('结束时间(例如20190830):')
        s_city = src_citys[s_city]
        d_city = dst_citys[d_city]

        url = 'http://s.tuniu.com/search_complex/whole-sh-0-%E7%83%AD%E9%97%A8/list-{}-b4-{}_{}-{}'.format(s_city, start_time, end_time, d_city)
        yield scrapy.Request(
            url=url,

            callback=self.parse_html
        )

    def parse_html(self, response):
        r_list = response.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[1]/ul/li')
        print(r_list)
        for r in r_list:
            item = TuniuItem()
            item['title']  = r.xpath('.//span[@class="main-tit"]/@name').get()
            item['link'] = 'http:' + r.xpath('.//div/a/@href').get()
            print(item['link'])
            item['price'] = r.xpath('//div/a/div/div[class="tnPrice"]/em/text()').get()
            new_pro = r.xpath('.//div/a/div/div/div[@class="new-pro"]').extract()
            if not len(new_pro):
                item['satisfaction'] = r.xpath('.//div[@class="comment-satNum"]//i/text()').get()
                item['travelNum'] = r.xpath('.//div/a/div/div/div[@class="trav-person"]/p[1]/i/text()').get()
                item['reviewNum'] = r.xpath('.//div/a/div/div/div[@class="trav-person"]/p[2]/i/text()').get()
            else:
                item['satisfaction'] = '新产品'
                item['travelNum'] = '新产品'
                item['reviewNum'] = '新产品'
            item['recommended'] = r.xpath('.//span[@class="overview-scenery"]/text()').get()
            item['supplier'] = r.xpath('/div/a/dl/dd/span[1]/span/text()').get()

            yield scrapy.Request(
                url=item['link'],
                meta={'item':item},
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
        item = response.meta['item']

        # 优惠信息
        item['coupons'] = "".join(response.xpath('//div[@class="detail-favor-coupon-desc"]/text()').extract())
        # 想办法获取评论的地址
        # 产品点评 + 酒店点评 + 景点点评
        product_id = response.url.split('/')[-1]
        url = 'http://www.tuniu.com/papi/tour/comment/product?productId={}&selectedType=0&stamp=097131909976971451566462242555'.format(product_id)
        # 产品点评
        yield scrapy.Request(
            url=url,
            callback=self.parse_three_html,
            meta={'item':item}
        )


    def parse_three_html(self, response):
        item = response.meta['item']
        html = response.text
        json_html = json.loads(html)
        comment = {}
        for i in json_html['data']['list']:
            comment[i['realName']] = i['content']
        item['cp_comments'] = comment
        yield item









