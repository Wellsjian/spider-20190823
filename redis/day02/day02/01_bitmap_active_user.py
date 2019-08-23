import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# user1: 一年中第5天和200天登录
r.setbit('user1',4,1)
r.setbit('user1',199,1)
# user2: 一年中第100天和第300天登录
r.setbit('user2',99,1)
r.setbit('user2',299,1)
# user3: 登录了100次以上
for i in range(1,366,2):
  r.setbit('user3',i,1)
# user4: 登录了100次以上
for i in range(1,366,3):
  r.setbit('user4',i,1)

user_list = r.keys('user*')

# 存放活跃用户列表
active_users = []
# 存放不活跃用户列表
no_active_users = []

for user in user_list:
  login_count = r.bitcount(user)
  if login_count >= 100:
    active_users.append((user,login_count))
  else:
    no_active_users.append((user,login_count))

print('活跃用户:',active_users)
print('不活跃用户:',no_active_users)
































