from selenium import webdriver
from PIL import Image
from day10.PythonHTTP.YDMHTTPDemo3 import *


class AttackYdm(object):

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://www.yundama.com/'

    # 1.获取网站截图.
    def get_index_shot(self):
        self.browser.get(self.url)
        self.browser.save_screenshot('index.png')

    # 2.从截取图片中获取验证码图片
    def get_caphe(self):
        # 锁定节点,获取坐标
        location = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').location
        print(location)
        # 大小
        size = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').size
        print(size)
        # 计算四个坐标
        left_x = location['x']
        left_y = location['y']
        right_x = left_x + size['width']
        right_y = left_y + size['height']

        # 截图
        image = Image.open('index.png').crop((left_x, left_y, right_x, right_y))
        image.save('caphe.png')

    # 3.在线获取验证码
    def get_code(self):
        result = get_index('caphe.png')
        print(result)

    def main(self):
        self.get_index_shot()
        self.get_caphe()
        self.get_code()

if __name__ =="__main__":
    spider = AttackYdm()
    spider.main()
