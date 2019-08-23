from selenium import webdriver
import pymysql
from queue import Queue
from threading import Thread


class GovSpider(object):

    def __init__(self):
        # 无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.options)
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='123456',
            database='govement',
            charset='utf8'
        )
        self.cur = self.db.cursor()
        self.province_list = []
        self.city_list = []
        self.county_list = []
        self.q = Queue()

    def create_thread(self, func):
        t_list = []
        for i in range(30):
            t = Thread(target=func)
            t_list.append(t)
            t.start()

        for j in t_list:
            j.join()

    def get_increment_link(self):
        self.browser.get(self.one_url)
        td = self.browser.find_element_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]')
        two_url = td.get_attribute('href')
        # del_sql = 'delete from url_info'
        sel_sql = 'select url from url_info where url=%s'
        # self.cur.execute(del_sql)
        # num  为返回的值  受到影响的rows
        num = self.cur.execute(sel_sql, [two_url])
        if num:
            print('已经存在')
        else:
            ins_sql = 'insert into url_info (url) values (url=%s)'
            self.cur.execute(ins_sql, [two_url])
            self.db.commit()
            td.click()
            # 切换页面  转换窗口浏览器对象
            all_handles = self.browser.window_handles
            self.browser.switch_to_window(all_handles[1])
            self.get_data()

    def get_data(self):
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(code, name)
            # 添加数据
            if code[-4:] == '0000':
                self.province_list.append([name, code])
                if name in ('北京市', '天津市', '上海市', '重庆市'):
                    self.city_list.append([name, code, code])
            elif code[-2:] == "00":
                self.city_list.append([name, code,(code[:2]+ "0000")])
            else:
                if code[:2] in ('11', '12', '31', '50'):
                    self.county_list.append([name, code, (code[:2] + "0000")])
                else:
                    self.county_list.append([name, code, (code[:4] + "00")])
        self.save_to_database()

    def save_to_database(self):
        p_del = 'delete from province'
        ct_del = 'delete from city'
        cy_del = 'delete from county'
        self.cur.execute(p_del)
        self.cur.execute(ct_del)
        self.cur.execute(cy_del)
        p_sql = 'insert into province(p_name,p_code) values(%s,%s)'
        ct_sql = 'insert into city(c_name,c_code,c_father_code) values(%s,%s,%s)'
        cy_sql = 'insert into county(x_name,x_code,x_father_code) values(%s,%s,%s)'
        self.cur.executemany(p_sql,self.province_list)
        self.cur.executemany(ct_sql, self.city_list)
        self.cur.executemany(cy_sql, self.county_list)
        self.db.commit()

    def main(self):
        self.get_increment_link()
        self.cur.close()
        self.db.close()
        self.browser.quit()


if __name__ == "__main__":
    spider = GovSpider()
    spider.main()
