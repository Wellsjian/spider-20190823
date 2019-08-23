from selenium import webdriver
import time
from threading import Thread


class JdSpider(object):

    def __init__(self):
        self.url = 'https://www.jd.com/'
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Firefox(options=self.options)

    # 获取具体的商品页信息
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        self.count = 0
        time.sleep(3)

    def create_thread(self, func):
        t_list = []
        for i in range(30):
            t = Thread(target=func)
            t_list.append(t)
            t.start()

        for j in t_list:
            j.join()

    def parse_html(self):
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        item = {}
        for li in li_list:
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]').text.strip()
            item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            print(item)
            self.count +=1

    def get_more_data(self):
        while True:
            # while True:
            self.parse_html()
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            else:
                break

    def main(self):
        self.get_html()

        self.get_more_data()

        print('数量：', self.count)

if __name__ == "__main__":
    spider = JdSpider()
    spider.main()
