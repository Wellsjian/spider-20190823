from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.mca.gov.cn/article/sj/xzqh/2019//')
eles = browser.find_elements_by_xpath('//a[@class="artitlelist"]')
for ele in eles:
    if ele.text.endswith('代码'):
        ele.click()
        code = browser.find_element_by_class_name('xl7111159')
        name = browser.find_element_by_class_name('xl7111159')
        print(code, name)






























