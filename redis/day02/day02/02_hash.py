'''设置1个字段,更改1个字段,设置多个字段,获取相关信息'''
import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# 设置
r.hset('user1','name','bujingyun')
# 更新
r.hset('user1','name','kongci')
# 取数据
print(r.hget('user1','name'))
# 一次设置多个field和value
user_dict = {
  'password':'123456',
  'gender':'F',
  'height':'165'
}
r.hmset('user1',user_dict)
# 获取所有数据,字典
print(r.hgetall('user1'))

# 获取所有fields和所有values
print(r.hkeys('user1'))
print(r.hvals('user1'))


























