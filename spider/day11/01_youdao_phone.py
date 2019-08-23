import re

import requests
from lxml import etree

url = 'https://m.youdao.com/translate'
word = input('请输入查询单词:')

data = {
    'inputtext': word,
    'type': 'AUTO'
}
html = requests.post(url=url, data=data).text
patterns = etree.HTML(html)
r_list = patterns.xpath('//*[@id="translateResult"]/li/text()')
data = r_list[0]
print(data)
#
# with open('123.html', 'w') as obj:
#     obj.write(html)