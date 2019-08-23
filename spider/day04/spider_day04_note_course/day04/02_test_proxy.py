'''使用代理IP访问测试网站,查看结果'''
import requests

url = 'http://httpbin.org/get'
proxies = {
  'http':'http://309435365:szayclhp@43.226.164.156:16818',
  'https':'https://309435365:szayclhp@43.226.164.156:16818'
}
# proxies = {
#   'http':'http://59.172.27.6:38380',
#   'https':'https://59.172.27.6:38380'
# }
# 发请求,获取响应内容,查看origin
html = requests.get(
  url=url,
  proxies=proxies,
  timeout=8
).text

print(html)






