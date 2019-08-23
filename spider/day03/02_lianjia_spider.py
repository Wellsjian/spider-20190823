import requests
import time
from lxml import etree
from user_agent import ua_list as u
import random

class LianJiaSpider(object):

    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}'
        self.blog = 1

    def __get_html(self, url):
        headers = {'User-Agent':random.choice(u)}
        if self.blog <= 3:
            try:
                res = requests.get(url, headers=headers, timeout=5)
                res.encoding = 'utf-8'
                html = res.text
                self.__parse_html(html)
            except:
                print('尝试重新连接')
                self.blog += 1
                self.__get_html(url)

    def __parse_html(self, html):
        parse_html = etree.HTML(html)

        r_list = parse_html.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        item = {}
        for r in r_list:
            name_list = r.xpath('.//a[@data-el="region"]/text()')
            item['name'] = [name_list[0].strip() if name_list else None][0]
            # 户型 + 面积 + 方位 + 是否精装
            info_xpath = r.xpath('.//div[@class="houseInfo"]/text()')
            info_list = [info_xpath[0].strip().split("|") if info_xpath else None][0]

            if len(info_list) == 5:
                item['model'] = info_list[1]
                item['area'] = info_list[2]
                item['direction'] = info_list[3]
                item['perfect'] = info_list[4]
            else:
                item['model'] = item['area'] = item['direction'] = item['perfect'] = None
            # 楼层
            floor_list = r.xpath('.//div[@class="positionInfo"]/text()')
            item['floor'] = [floor_list[0].strip().split()[0] if floor_list else None]
            #区域
            address_list = r.xpath('.//div[@class="positionInfo"]/a/text()')
            item['address'] = address_list[0].strip()
            #总价
            total_price_list = r.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total_price'] = [total_price_list[0].strip() if total_price_list else None]
            #单价
            unit_price_list = r.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit_prcie'] = [unit_price_list[0].strip() if unit_price_list else None]

            print(item)

    def main(self):
        for page in range(1,2):
            url = self.url.format(page)
            self.__get_html(url)
            time.sleep(random.uniform(1,2))
            self.blog = 1


if __name__ =="__main__":
    spider = LianJiaSpider()
    spider.main()


















