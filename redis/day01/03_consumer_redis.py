import redis
import time
import random

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

while True:
    url = r.brpop('spider:urls', 5)[1]
    print(url)
    if url:
        print('正在抓取', url.decode())
    else:
        break

r.delete('spider:urls')