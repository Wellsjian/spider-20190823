# 1.导入模块
from urllib import request
from urllib import parse


# 2.拼接URL
def get_url(word):
    url = 'http://www.baidu.com/s?wd={}'

    params = parse.quote(word)

    url = url.format(params)

    return url


# 发送请求， 接收响应 ， 保存文件
def request_url(word):
    url = get_url(word)
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64;'
                      ' Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; '
                      '.NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }

    #创建请求内容
    req = request.Request(url=url, headers=headers)
    #发送请求，接收响应
    res = request.urlopen(req)
    #读取响应内容
    html = res.read().decode()
    #打开文件
    with open('{}.html'.format(word), 'w', encoding='utf-8') as obj:
        obj.write(html)

if __name__ == "__main__":
    word = input("请输入查找内容：")
    request_url(word)
