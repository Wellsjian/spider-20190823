import redis
import pymysql

# 1.先到redis数据库中查询
# 2.如果1 没有  则去MySQL数据库查询  缓存在redis中

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

username = input('请输入查询名：')

user = r.hgetall('user')

if user:
    print(user)
else:
    # redis 中没有缓存  需要去MySQL中查询

    db = pymysql.connect(host='localhost',
                         user="root",
                         port=3306,
                         password='123456',
                         database='redis',
                         charset='utf8')
    cursor = db.cursor()
    sql = 'select username,age,gender from user where username=%s'
    # try:
    cursor.execute(sql,[username,])
    res = cursor.fetchall()  # 得到的结果为元组，一条记录为一个小元组（（））
    if not res:
        print('用户不存在')
    else:
        # 打印输出
        print('mysql', res)
        # 缓存到redis数据库中
        user_dict = {
            'username': res[0][0],
            'age': res[0][1],
            'gender': res[0][2]
        }
        r.hmset('user', user_dict)
        # 设置过期时间
        r.expire('user', 30)
    # except  Exception as e:
    #     print(e)
    #     db.rollback()
    #
