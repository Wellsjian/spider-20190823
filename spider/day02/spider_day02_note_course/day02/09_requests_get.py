import requests

url = 'http://www.baidu.com/'
headers = {
  'User-Agent':'Mozilla/5.0'
}
res = requests.get(url=url,headers=headers)
# 显示编码
res.encoding = 'utf-8'
# 获取文本内容 - string
html = res.text
# 获取文本内容 - bytes
byte = res.content
# 获取HTTP响应码
code = res.status_code
# 返回实际数据的URL地址
url = res.url






















