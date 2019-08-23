import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.set('username', 'guods')

r1 = r.get('username')
print(r1)

r.mset({'username':'xiaoze', 'password':'123456'})
print(r.mget('username', 'password'))

print(r.strlen('username'))

r.delete('username')

r.set('age','25')
print(r.incrby('age',10))

r.set('age','25')
print(r.decrby('age',10))

r.set('age','25')
print(r.incr('age',10))

r.set('age','25')
print(r.decr('age',10))

print(r.incrbyfloat('age', 3.654))


