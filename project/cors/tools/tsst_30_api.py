from threading import Thread
import random
import requests

'''
发送30个请求   向8000   8001  随机发送请求
'''

def get_request():
    url1 = 'http://127.0.0.1:8000/test'
    url2 = 'http://127.0.0.1:8001/test'
    url = random.choice([url1, url2])
    # 发送请求
    requests.get(url)

tlist = []
#创建并发，
for i in range(30):
    t = Thread(target=get_request)
    tlist.append(t)
    t.start()

#回收进程
for j in tlist:
    j.join()

