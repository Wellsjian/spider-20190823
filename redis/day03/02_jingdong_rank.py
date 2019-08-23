
import  redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

day01 = {
    'huawei':5000,
    'oppo':4000,
    'iphone':3000
}

day02 = {
    'huawei':5200,
    'oppo':4340,
    'iphone':3460
}


day03 = {
    'huawei':5740,
    'oppo':4680,
    'iphone':3860
}

r.zadd('mobile-01', day01)
r.zadd('mobile-02', day02)
r.zadd('mobile-03', day03)

r.zunionstore('mobile-001:003',('mobile-01', 'mobile-02', 'mobile-02'), aggregate='max')

list = r.zrevrange('mobile-001:003', 0, 2, withscores=True)

for i in range(len(list)):
    print('{}:{}'.format(list[i][0].decode(), int(list[i][1])))











