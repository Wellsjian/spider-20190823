from urllib import request, parse
import time
import random
import re
from user_agent import ua_list as u


class SecondView(object):
    """
    爬取二级页面
    """

    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

    # 1. 获取响应数据html
    def __get_html(self, url):
        headers = {'User-Agent': random.choice(u)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('gb2312','ignore')
        return html

    # 2.解析正则
    def __re_func(self, re_bds, html):
        pattern = re.compile(re_bds, re.S)
        data_list = pattern.findall(html)
        return data_list

    # 3.提取一级界面解析数据  多级数据实现一一对应
    # html 是一级响应到的数据html
    def __parse_first_view_data(self, html):
        re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">(.*?)</a>.*?</table>'
        first_view_data_list = self.__re_func(re_bds, html)
        item = {}
        for data in first_view_data_list:
            item['name'] = data[1].sprit()
            link = 'https://www.dytt8.net' + data[0].strip()
            item['download'] = self.__parse_second_view_data(link)
            print(item)

    # 提取二级界面数据  实现数据一一对应
    def __parse_second_view_data(self, link):
        html = self.__get_html(link)
        re_bds = r'<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        second_view_data_list = self.__re_func(re_bds, html)
        download = second_view_data_list[0].strip()
        return download

    # 4.主函数， 启动服务<td style="WORD-WRAP.*?>.*?>(.*?)</a>
    def main(self):

        for page in range(1, 11):
            url = self.url.format(page)
            html = self.__get_html(url)
            self.__parse_first_view_data(html)
            time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    spider = SecondView()
    spider.main()
