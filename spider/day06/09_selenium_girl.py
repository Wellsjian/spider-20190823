import time

from selenium import webdriver

#1.创建浏览器对象
browser = webdriver.Firefox()
#2.打开浏览器， 输入‘http://www.baidu.com’
browser.get('http://www.baidu.com')
#3. 找到搜索框 输入查找内容
# browser.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
# time.sleep(1)
#4.找到按钮 发送请求
# browser.find_element_by_xpath('//*[@id="su"]').click()
# time.sleep(20)
#查看访问页源码
html = browser.page_source
# print(html)
## 从html源码中搜索指定字符串,没有找到返回：-1
html1 = browser.page_source.find('11111111111')
print(html1)

#5.关闭浏览器
browser.quit()