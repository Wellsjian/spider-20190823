import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from user import models



# Create your views here.



def tokens_view(request, ):
    """
    登录函数
    :param request:
    :return: 返回JSON对象
    """
    if not request.method == 'POST':
        result = {'code': 102, 'error': 'Please use POST'}
        return JsonResponse(result)
    json_str = request.body
    if not json_str:
        result = {'code': 202, 'error': '请求为空'}
        return JsonResponse(result)
    data = json.loads(json_str.decode())
    username = data.get('username')
    if not username:
        result = {'code': 203, 'error': '请求中未提交用户名'}
        return JsonResponse(result)
    old_name = models.UserProfile.objects.filter(username=username)
    password1 = old_name[0].password
    if not old_name:
        result = {'code': 208, 'error': '用户名或密码错误'}
        return JsonResponse(result)
    password = data.get('password')
    if not password:
        result = {'code': 205, 'error': '请求中未提交密码'}
        return JsonResponse(result)
    p_w = hashlib.sha256()
    p_w.update(password.encode())
    password = p_w.hexdigest()
    if not password == password1:
        result = {'code': 206, 'error': '用户名或密码错误'}
        return JsonResponse(result)
    token = make_token(username, expire=3600 * 24)
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
    return JsonResponse(result)




def make_token(username, expire=3600 * 24):
    """

    :param username:
    :param expire:
    :return:
    """
    key = '123456789asd'
    now = time.time()
    data = {'username': username, 'exp': int(now + expire)}
    return jwt.encode(data, key, algorithm='HS256')
