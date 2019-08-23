from django.http import HttpResponse
from user import models
import redis


def test_view(request):
#     pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
#     r = redis.Redis(connection_pool=pool)
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    print(r)
    while True:
        try:
            with r.lock('王大大', blocking_timeout=3) as lock:

        #对字段 score  进行  +1  操作
                user = models.UserProfile.objects.get(username='王大大')
                user.score += 1
                user.save()
            break
        except Exception as e:
            print(e)
            print('获得锁失败')

    
    return HttpResponse('Hi Hi Hi')
