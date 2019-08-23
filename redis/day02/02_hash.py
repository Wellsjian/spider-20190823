import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

#设置
r.hset('user1', 'name', '123')
r.hset('user1', 'name', '456')

print(r.hget('user1', 'name'))

print()