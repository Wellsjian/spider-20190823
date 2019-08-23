# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#导入Scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class SoPipeline(ImagesPipeline):
    # 重写ImagesPipeline的get_media_requests方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_url'],
            meta={'item':item['img_title']}
        )

    def file_path(self, request, response=None, info=None):

        img_title = request.meta['item']
        jpg = request.url.split('.')[-1]
        filename = img_title + '.' + jpg
        return filename




