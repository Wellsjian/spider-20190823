import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 有序集合添加元素。初始化元素
r.zadd('ranking', {'song1': 1, 'song2': 1, 'song3': 1, 'song4': 1})
r.zadd('ranking', {'song5': 1, 'song6': 1, 'song7': 1, 'song8': 1})

# 指定元素添加分值
r.zincrby('ranking', 50, 'song3')
r.zincrby('ranking', 80, 'song5')
r.zincrby('ranking', 70, 'song8')
r.zincrby('ranking', 40, 'song6')

# 结果为  [(,),(,)  ]
list = r.zrevrange('ranking', 0, 2, withscores=True)
print(int(list[0][1]))
for i in range(len(list)):
    print(int(list[i][1]))
    print('第%s名:%s 播放次数：%s'%(i+1, list[i][0].decode(), int(list[i][1])))
    print('第{}名:{} 播放次数：{}'.format(i+1, list[i][0].decode(),int(list[i][1])))
