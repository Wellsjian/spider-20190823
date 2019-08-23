# from selenium.webdriver import ActionChains
from  selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
# browser.find_element_by_id('kw').send_keys('赵丽颖')
element = browser.find_elements_by_name('tj_settingicon')[1]
print(element.text)

# 把鼠标移动到设置节点
actions = webdriver.ActionChains(browser)
actions.move_to_element(element)
actions.perform()

#找到 高级设置按钮 点击
browser.find_element_by_link_text('高级搜索').click()
