import redis
import pymysql


def update_mysql(username, age):
    db = pymysql.connect(
        host="localhost",
        user='root',
        port=3306,
        password='123456',
        database='redis',
        charset='utf8'
    )
    cur = db.cursor()
    sql = 'update user set age=%s where username=%s'
    try:
        code = cur.execute(sql, [age, username])
        db.commit()
        if code == 1:
            return True
    except Exception as e:
        print('Error', e)
        db.rollback()
    cur.close()
    db.close()


def update_redis(age):
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.hset('user', 'age', age)
    print('已同步到redis')
    # 设置过期时间  expire
    r.expire('user', 300)

    print(r.hget('user', 'age'))


if __name__ == "__main__":
    username = input("请输入用户名：")
    age = input("请输入更改后的年龄：")
    if update_mysql(username, age):
        update_redis(age)
    else:
        print('用户名有误')
