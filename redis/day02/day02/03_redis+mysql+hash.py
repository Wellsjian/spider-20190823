import redis
import pymysql

# 1. 先到redis中查询
# 2. redis中没有,到mysql查询,缓存到redis(设置过期时间)
# 3. 再查询1次
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
username = input('请输入用户名:')

result = r.hgetall('user')
if result:
  print(result)
else:
  # redis中没有缓存,需要到mysql中查询
  db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='userdb',
    charset='utf8'
  )
  cursor = db.cursor()
  sele = 'select username,age,gender from user where ' \
         'username=%s'
  cursor.execute(sele,[username])
  # userinfo: (('guoxiaonao',36,'M'),)
  userinfo = cursor.fetchall()
  if not userinfo:
    print('用户不存在')
  else:
    # 打印输出
    print('mysql',userinfo)
    # 缓存到redis
    user_dict = {
      'username':userinfo[0][0],
      'age':userinfo[0][1],
      'gender':userinfo[0][2]
    }
    r.hmset('user',user_dict)
    # 设置过期时间
    r.expire('user',30)









# key:user

# filed: username
# filed: password
# filed: gender
# filed: age



















