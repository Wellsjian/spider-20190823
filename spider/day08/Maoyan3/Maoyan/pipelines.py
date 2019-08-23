# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['star'], item['time'])
        return item

import pymysql
from .settings import *
#自定义管道  MySql 数据库
class MaoyanMySqlPipeline(object):
    #爬虫项目开始执行时执行此函数
    def open_spider(self, spider):
        #一般用于建立数据库连接 执行1遍
        print('开始吧')
        self.db = pymysql.connect(
            host = MYSQL_HOST,
            port = MYSQL_PORT,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            database = MYSQL_DB,
            charset = MYSQL_CHARSET
        )
        self.cur = self.db.cursor()
    def process_item(self, item, spider):
        l = [item['name'], item['star'], item['time']]
        try:
            ins_sql = 'insert into data values (%s,%s,%s)'
            self.cur.execute(ins_sql, l)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('跑错啦')
        return item

    def close_spider(self, spider):
        print('结束吧')
        #一般用于断开数据库连接
        self.cur.close()
        self.db.close()
