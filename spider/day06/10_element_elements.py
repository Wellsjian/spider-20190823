from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.qiushibaike.com/text/')
div = browser.find_element_by_class_name('content')

print(div.text)

divs = browser.find_elements_by_class_name('content')
for div in divs:
    print('\033[36m------------------------\033[0m')
    print("*"*60)
    print(div.text)
    print('*'*60)