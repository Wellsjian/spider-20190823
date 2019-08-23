# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        diractory = '/home/tarena/materials/xiaojian/novel/'
        content = item['content']
        filename = diractory + item['title']
        with open(filename, 'a') as obj:
            obj.write(content)
        return item
