# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class SoPipeline(ImagesPipeline):
    # 重写ImagesPipeline中的get_media_requests()方法
    def get_media_requests(self, item, info):
        # meta随着包装好的请求一起交给了调度器
        yield scrapy.Request(
            url=item['img_url'],
            meta={ 'item' : item['img_title'] }
        )

    # 重写file_path()方法: 指定路径以及文件名
    def file_path(self, request, response=None, info=None):
        img_title = request.meta['item']
        filename = img_title + '.' + \
                      request.url.split('.')[-1]

        return filename









