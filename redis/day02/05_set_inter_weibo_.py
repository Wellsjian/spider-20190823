import json

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# user1  关注的人
r.sadd('user1:focus', 'peiqi', 'danni')

# user2  关注的人
r.sadd('user2:focus', 'peiqi', 'danni', 'lingyang')

focus_set = r.sinter('user1:focus', 'user2:focus')

result = set()
for i in focus_set:
    result.add(i.decode())
print(result)

