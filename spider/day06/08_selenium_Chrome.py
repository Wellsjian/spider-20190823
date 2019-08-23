from  selenium import webdriver
import time

# 创建浏览器对象
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')


browser.save_screenshot('baidu.png')

#关闭浏览器
browser.quit()
