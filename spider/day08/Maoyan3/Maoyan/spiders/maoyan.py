# -*- coding: utf-8 -*-
import scrapy
from items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan3'
    allowed_domains = ['maoyan.com']


    def start_requests(self):
        for offset in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset={}'.format(str(offset))
            # 把地址交给调度器入队列
            yield scrapy.Request(url=url,callback=self.parse_html )

    def parse_html(self, response):
        item = MaoyanItem()

        # 基准xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()
            print('*' * 50)
            # 将生成器对象交给管道文件处理
            yield item

