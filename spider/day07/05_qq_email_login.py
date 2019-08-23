from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://en.mail.qq.com/')

login_frame = browser.find_element_by_id('login_frame')
browser.switch_to_frame(login_frame)

#qq 密码登录
browser.find_element_by_id('u').send_keys('2621470058')
browser.find_element_by_id('p').send_keys('zhanshen001')
browser.find_element_by_id('login_button').click()






