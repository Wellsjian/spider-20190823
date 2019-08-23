import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 用户     登录
# user1   5   200
# user2   100 300
# user3   >100
# user4   >100天

r.setbit('user1', 4, 1)
r.setbit('user1', 199, 1)

r.setbit('user2', 99, 1)
r.setbit('user2', 299, 1)

for i in range(0, 365, 2):
    r.setbit('user3', i, 1)

for i in range(1, 365, 2):
    r.setbit('user4', i, 1)

list01 = []  # 活跃用户
list02 = []  # 不活跃用户
for user in r.keys('user*'):
    count = r.bitcount(user)
    if count > 100:
        list01.append((user,count))

    else:
        list02.append((user,count))

print(list01)
print(list02)