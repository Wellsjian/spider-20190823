import redis
import django

r = redis.Redis(host='localhost', port=6379, db=0)

r.zadd('salary1', {'lina':8000,'lily':10000, 'mary':12000})

print(r.zrange('salary1', 0, -1, desc=True))

print(r.zrangebyscore('salary1', 6000, 9000))