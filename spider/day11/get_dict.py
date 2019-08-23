import requests
from lxml import etree

url = 'http://s.tuniu.com/search_complex/whole-sh-0-%E7%83%AD%E9%97%A8/'

html = requests.get(url=url).text

#目的地
pattern = etree.HTML(html)
r_list = pattern.xpath('//*[@id="niuren_list"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/dl/dd/ul/li')
dst_citys = {}
for r in r_list[1:]:
    m_name = r.xpath('./a/text()')[0].strip()
    m_code = r.xpath('./a/@href')[0].strip().split("-")[-1]
    dst_citys[m_name] = m_code

r_list1 = pattern.xpath('//*[@id="niuren_list"]/div[2]/div[1]/div[2]/div[1]/div/div[3]/dl/dd[@class="onlyOneLine"]/ul/li')
src_citys = {}
for r in r_list1[1:]:
    m_name = r.xpath('./a/text()')[0].strip()
    m_code = r.xpath('./a/@href')[0].strip().split("-")[-1]
    src_citys[m_name] = m_code




