
import requests

headers = {
    'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
}
url = 'http://b-ssl.duitang.com/uploads/item/201510/02/20151002174625_wmKPM.jpeg'
res = requests.get(url=url, headers=headers)
html = res.content

with open('girl.jpeg', 'wb+') as obj:
    obj.write(html)