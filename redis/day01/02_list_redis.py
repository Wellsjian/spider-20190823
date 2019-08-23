import redis

r = redis.Redis(host="localhost", port=6379, db=0 )

r.rpush('Python课程','python基础', 'python高级', '网络编程', 'web前端', 'Django框架')

r .linsert('Python课程','before', 'python高级', 'spider')

print(r.llen('Python课程'))

for key in r.lrange('Python课程', 0, -1):
    print(key.decode())


while True:
    result = r.brpop('Python课程', 3)
    if result:
        for re in result:
         print(re.decode())
    else:
        break

r.delete('Python课程')