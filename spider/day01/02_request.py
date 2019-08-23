from urllib import request

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
}

#1.创建请阿牛对象
req = request.Request(url=url, headers=headers)

#2.获取响应对象
res = request.urlopen(req)

#3.读取响应内容

html = res.read().decode('utf-8')

print(html)

