import redis
import time
import random


r = redis.Redis(host="127.0.0.1", port=6379, db=0)
#生产者开始生产URL地址
for page in range(0,67):
    url = 'http:/app.mi.com/category/%s'%page
    r.lpush('spider:urls', url)
    time.sleep(random.randint(1,3))

r.delete('spider:urls')



