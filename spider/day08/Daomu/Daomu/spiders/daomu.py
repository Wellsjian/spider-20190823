# -*- coding: utf-8 -*-
import os

import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    path = '/home/tarena/materials/xiaojian/novel/'
    if not os.path.exists(path):
        os.makedirs(path)

    def parse(self, response):
        #解析界面, 提取连接, 交给调度器
        # print(response)
        li_list = response.xpath("//li[contains(@id,'menu-item-20')]/a/@href").extract()
        print(li_list)
        for li in li_list:

            yield scrapy.Request(
                url=li,
                callback=self.parse_two_html
            )


    def parse_two_html(self, response):
        #基准 xpath
        article_list = response.xpath('//article')
        for article in article_list:
            item = DaomuItem()
            item['title'] = article.xpath('./a/text()').get()
            link = article.xpath('./a/@href').get()
            #把链接发送给调速器
            yield scrapy.Request(
                url=link,
                #在不同解析函数之间 传递item
                meta={'item':item},
                callback=self.parse_three_html
            )


    def parse_three_html(self, response):
        item = response.meta['item']
        content_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = "\n".join(content_list)
        print(item['title'], item['content'])

        yield item