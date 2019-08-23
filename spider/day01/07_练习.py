import re
import time
import random
from urllib import request
import user_agent


class Spider_(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # 获取请求
    def get_request(self, url):
        headers = {'User-Agent': random.choice(user_agent.ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 提取数据
    def extract_data(self, html):
        pattern = re.compile(r'''class="name".*?Id:\d+}">(.*?)</a>.*?star">(.*?)</p>.*?time">(.*?)</p>''', re.S)
        rlist = pattern.findall(html)
        with open('data.txt', 'a+', encoding='utf-8') as obj:
            for r in rlist:
                s = '{}  {}  {} \n'
                data = s.format(r[0].strip(), r[1].strip(), r[2].strip())
                obj.write(data)
                obj.flush()

                # s = '电影名称:{}  主演:{}  上映时间:{}'
                print(data)


        # 保存数据

    def save_response(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as obj:
            obj.write(html)

    # 启动服务
    def main(self):
        start = int(input("请输入开始页："))
        end = int(input("请输入结束页："))
        for page in range(start, end + 1):
            offect1 = (page - 1) * 10
            url = self.url.format(offect1)
            html = self.get_request(url)
            # filename = '猫眼电影-第{}页.html'.format(page)
            # self.save_response(filename, html)
            self.extract_data(html)

            time.sleep(random.randint(1, 3))
            # print('猫眼电影-第{}页 爬取成功'.format(page))


if __name__ == "__main__":
    spider = Spider_()
    spider.main()


