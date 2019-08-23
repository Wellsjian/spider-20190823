# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *


class TengxunzhaopingPipeline(object):


    def process_item(self, item, spider):
        return item


class TengxunzhaopingMySqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            charset=MYSQL_CHARSET
        )
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into tencenttab values(%s, %s, %s, %s, %s, %s)'
        l = [
            item['job_name'],
            item['job_type'],
            item['job_duty'],
            item['job_require'],
            item['job_address'],
            item['job_time']
        ]
        self.cur.execute(sql, l)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()