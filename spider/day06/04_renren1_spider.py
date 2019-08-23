import requests


class RenRenSpider(object):
    def __init__(self):
        self.url = ''
        self.headers = {
            'Cookie':'',
            'User-Agent':''
        }

    def __get_html(self):
        html = requests.get(url=self.url, headers=self.headers).text
        print(html)
        self.__parse_html(html)

    def __parse_html(self, html):
        pass


    def main(self):
        self.__get_html()

if __name__ =="__main__":
    spider = RenRenSpider()
    spider.main()
