from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def set_cookies_view(request):
    #方法一
    # resp = HttpResponse("OK")
    # resp.set_cookie("aaa",'bbb')
    # return resp
    #方法二
    resp = render(request,"test.html",locals())
    resp.set_cookie("123",'王大大')
    return resp
def get_cookies_view(request):
    value = request.COOKIES.get('aaa',"cookies")
    return HttpResponse(value)
