from urllib import request
from urllib import parse
import time
import random
import user_agent


class Tieba(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'

    # 获取响应内容
    def get_response(self, url):
        headers = {'User_Agent': random.choice(user_agent.ua_list)}
        #获取请求
        req = request.Request(url=url, headers=headers)
        #
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 解析响应， 获取数据
    def parse_response(self):
        pass

    # 保存数据， 数据分析
    def save_response(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as obj:
            obj.write(html)

    # 主函数，用于提供接口启动功能
    def main(self):
        name = input('请输入贴吧名：')
        start = int(input("请输入起始页："))
        end = int(input("请输入结束页："))

        kw = parse.quote(name)
        for page in range(start, end + 1):
            pn = 50 * (page - 1)
            url = self.url.format(kw, pn)
            filename = '{}-第{}页.html'.format(name, page)
            html = self.get_response(url)
            self.save_response(filename, html)
            time.sleep(random.randint(1, 3))
            print('第{}页爬取成功'.format(page))
            t


if __name__ == "__main__":
    start = time.time()
    spider = Tieba()
    spider.main()
    end = time.time()
    print('执行时间为:%0.2f'%(end - start))
