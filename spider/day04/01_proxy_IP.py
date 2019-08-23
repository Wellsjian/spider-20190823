import IP
import requests

'''
测试代理IP的可用性'''


url = 'http://httpbin.org/get'
for i in IP.ip:
    list01 = i.split(":")
    ip = list01[0]
    port = list01[1]
    # print(ip, port)

    try:
        proxies = {
            'http':'http://{}:{}'.format(ip,port),
            'https':'https://{}:{}'.format(ip,port)
        }
        html = requests.get(url=url, proxies=proxies, timeout=5).text
        print(html)
        print(ip,port)
    except:
        print('failed')
        continue




