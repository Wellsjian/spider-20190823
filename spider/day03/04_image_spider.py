from lxml import etree
import random
import time
import requests
from urllib import parse
from user_agent import ua_list as u
import os

class ImageSpider(object):

    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'

    def __get_html(self, url):
        headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        res = requests.get(url, headers=headers)
        res.encoding = "utf-8"
        html = res.content.decode('utf-8', 'ignore')
        return html

    def __xpath_func(self, html, xpath_bds):
        path_html = etree.HTML(html)
        r_list = path_html.xpath(xpath_bds)
        return r_list

    def __parse_html(self, url):
        html = self.__get_html(url)
        xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href |  //div[@class="video_src_wrapper"]/embed/@data-video'
        r_list = self.__xpath_func(html, xpath_bds)
        # print(r_list)
        for r in r_list:
            # 拼接  帖子的URL地址
            t_url = 'http://tieba.baidu.com' + r
            # 把帖子所有图片保存到本地Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)
            self.__get_image(t_url)
            time.sleep(random.randint(1, 2))

    def __get_image(self, t_url):
        html = self.__get_html(t_url)
        # 图片的Xpath 表达式  + 视频链接
        # xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        xpath_bds = '//div[@class="video_src_wrapper"]/embed/@data-video'
        img_list = self.__xpath_func(html, xpath_bds)
        print(img_list)
        for img in img_list:
            html_bytes = requests.get(img, headers={'User-Agent':random.choice(u)}).content
            self.__save_html(img, html_bytes)

    def __save_html(self, img, html_bytes):
        filename = img[-10:]
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        dir = os.path.join(BASE_DIR, 'view_spider') + "/" + filename
        # path = os.path.join(BASE_DIR, )
        with open(dir , 'wb') as obj:
            obj.write(html_bytes)
            print('%s下载成功' % filename)

    def main(self):
        filename = input("请输入贴吧名：")
        kw = parse.urlencode({'kw': filename})
        start = int(input("请输入起始页"))
        end = int(input("请输入结束页"))
        for page in range(start, end):
            pn = (page - 1) * 50
            url = self.url.format(kw, pn)
            self.__parse_html(url)


if __name__ == "__main__":
    spider = ImageSpider()
    spider.main()
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# dir = os.path.join(BASE_DIR, 'img_spider') + "/123"
# print(dir)