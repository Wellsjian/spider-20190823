# -*- coding: utf-8 -*-
import scrapy
from items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    offset = 0
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):
        item = MaoyanItem()
        print('*' * 50)
        # 基准xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        print(dd_list)
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()

            # 将生成器对象交给管道文件处理
            yield item

        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(str(self.offset))

            yield scrapy.Request(
                url=url,
                callback=self.parse
            )