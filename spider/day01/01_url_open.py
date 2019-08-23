from urllib import request

response = request.urlopen('http://httpbin.org/get')

#获取响应内容
html = response.read().decode('utf-8')

#获取响应码
code = response.getcode()
print(code)

#获取返回实际数据的URL地址
url = response.geturl()
print(html)