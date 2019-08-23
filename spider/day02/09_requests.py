import requests

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
}

res = requests.get(url=url, headers=headers)
#显示编码
# res.encoding = 'utf-8'
#显示字符串文本
# print(res.text)
#显示字节串文本
# print(res.content)
# 显示响应状态码
# print(re s.status_code)
#显示访问路由
print(res.url)