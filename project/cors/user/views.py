import hashlib
import time

import jwt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from ctoken.views import make_token
from tools.login_check import login_check
from . import models
import json


# Create your views here.

@login_check('PUT')
def users_view(request, username=None):
    if request.method == "POST":
        json_str = request.body
        if not json_str:
            result = {'code': 202, 'error': 'Please POST data !!'}
            return JsonResponse(result)

        data = json.loads(json_str.decode())
        username = data.get('username')
        if not username:
            result = {'code': 203, 'error': 'Please write username !!'}
            return JsonResponse(result)
        email = data.get('email')
        if not email:
            result = {'code': 204, 'error': 'Please write email !!'}
            return JsonResponse(result)
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')
        if not password_1 or not password_2:
            result = {'code': 205, 'error': 'Please write password !!'}
            return JsonResponse(result)
        if password_1 != password_2:
            result = {'code': 206, 'error': 'Please write right password !!'}
            return JsonResponse(result)
        old_user = models.UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 207, 'error': 'The username is used !!'}
            return JsonResponse(result)
        p_m = hashlib.sha256()
        p_m.update(password_1.encode())
        try:
            models.UserProfile.objects.create(
                username=username,
                nickname=username,
                email=email,
                password=p_m.hexdigest(),
            )
        except Exception as e:
            print("Error is %s" % e)
        token = make_token(username, expire=3600 * 24)
        result = {"code": 200, "username": username, "data": {"token": token.decode()}}
        return JsonResponse(result)
    elif request.method == "GET":
        # 获取数据
        # 获取单个数据
        if username:
            users = models.UserProfile.objects.filter(username=username)
            print(users)
            if not users:
                result = {"code": 208, "error": 'The username is exited'}
                return JsonResponse(result)
            user = users[0]
            if request.GET.keys():
                data = {}
                for key in request.GET.keys():
                    if key == "password":
                        continue
                    if hasattr(user, key):
                        if key == 'avatar':
                            data[key] = str(getattr(user, key))
                        else:
                            data[key] = getattr(user, key)
                        data[key] = getattr(user, key)
                result = {"code": 200, "username": username, 'data': data}
                return JsonResponse(result)
            else:
                result = {'code': 200, 'username': username,
                          'data': {
                              'info': user.info,
                              'sign': user.sign,
                              'nickname': user.nickname,
                              'avatar': str(user.avatar)
                          }}
            return JsonResponse(result)
        else:
            all_users = models.UserProfile.objects.all()
            result = []
            for u in all_users:
                d = {}
                d['username'] = u.username
                d['nickname'] = u.nickname
                d['sign'] = u.sign
                d['info'] = u.info
                d['email'] = u.email
                d['avatar'] = str(u.avatar)
                result.append(d)
                return JsonResponse({'code': 200, 'data': result})
    elif request.method == "PUT":
        # 127.0.0.1:8000/v1/users/<username>
        user = request.user
        json_str = request.body
        data = json.loads(json_str.decode())
        nickname = data.get('nickname')
        if not nickname:
            result = {'code':210, 'error':'The nickname can not be none !!'}
            return JsonResponse(result)
        sign = data.get('sign')
        if sign is None:
            result = {'code':211, 'error':'The sign is not in json !!'}
            return JsonResponse(result)
        info = data.get('info')
        if info is None:
            result = {'code':212, 'error':'The info is not in json !!'}
            return JsonResponse(result)

        if user.username != username:
            result = {'code':213, 'error':'This is wrong !!'}
            return JsonResponse(result)
        #修改数据库中的数据
        user.info = info
        user.sign = sign
        user.nickname = nickname
        user.save()
        result = {'code':200, 'username':username}
        return JsonResponse(result)


@login_check('POST')
def avatar_view(request, username=None):
    if request.method != "POST":
        result = {'code':214, 'error':'Please use POST'}
        return JsonResponse(result)
    user = request.user
    if user.username != username:
        result = {'code':215, 'error':'you are wrong !!!'}
        return JsonResponse(result)
    avatar = request.FILES.get('avatar')
    if not avatar:
        result = {'code':216, 'error':'Please give me the avatar'}
        return JsonResponse(result)
    user.avatar = avatar
    user.save()
    result = {'code':200, 'username':username}
    return JsonResponse(result)






# def check_token(request):
#     token = request.META.get('HTTP_AUTHORIZATION')
#     if not token:
#         return None
#     key = '123456789asd'
#     try:
#         res = jwt.decode(token, key, algorithm='HS256')
#     except Exception as e:
#         print('check_token error is %s' %e)
#         return None
#
#     username = res['username']
#     users = models.UserProfile.objects.filter(username=username)
#     user = users[0]
#     return user