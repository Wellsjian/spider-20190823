import jwt
from django.http import JsonResponse

from user import models

TOKEN_KEY = '123456789asd'


def login_check(*methods):
    def _login_check(func):
        def wrapper(request, *args, **kwargs):
            # 获取token
            token = request.META.get('HTTP_AUTHORIZATION')
            if not methods:
                # 如果当前没有传 函数  则直接返回视图函数
                return func(request, *args, **kwargs)
            else:
                if not request.method in methods:
                    # 如果传参,检查当前参数是否在参数 methods 列表中
                    return func(request, *args, **kwargs)
                if not token:
                    result = {'code': 109, 'error': 'Please give me token'}
                    return JsonResponse(result)
                try:
                    res = jwt.decode(token, TOKEN_KEY)
                    # 抓指定异常
                # except jwt.ExpiredSignatureError(0)
                except Exception as e:
                    print('login_check is error %s' % e)
                    result = {'code': 108, 'error': 'The token is wrong'}
                    return JsonResponse(result)

                username = res['username']
                try:
                    user = models.UserProfile.objects.get(username=username)
                except:
                    user = None
                if not user:
                    result = {'code': 110, 'error': 'The user is not existed'}
                    return JsonResponse(result)
                # 将user  赋值给 request
                request.user = user
            return func(request, *args, **kwargs)

        return wrapper

    return _login_check


def get_user_by_request(request):
    """
    通过request  获取  user 
    :param request: 
    :return: 
    """
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res = jwt.decode(token, TOKEN_KEY)
    except Exception as e:
        return None
    username = res['username']
    try:
        user = models.UserProfile.objects.get(username=username)
    except Exception as e:
        return None
    if not user:
        return None
    return user
    
