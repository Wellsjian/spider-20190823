import redis
#创建redis  对象
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=0
)

key_list = r.keys('*')
for key in key_list:
    print(key.decode('utf-8'))
#返回1  0
r0 = r.exists('list01')
print(r0)
#b'list'
r1 = r.type('list')
print(r1)


r2 = r.lpush('list03', '1 2 3 4 5')
print(r2)