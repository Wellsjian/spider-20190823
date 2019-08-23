# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    #运行  scrapy crawl 爬虫名
    name = 'baidu'
    #允许爬取 的域名
    allowed_domains = ['www.baidu.com']
    #起始的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        #response 为百度的响应对象  提取百度一下
        xpath_bds = '/html/head/title/text()'
        # r_list  = response.xpath(xpath_bds).extract_first()
        # r_list  = response.xpath(xpath_bds).extract()
        r_list  = response.xpath(xpath_bds).get()

        print("*"*50)
        print(r_list)
        print("*"*50)
