import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def createXhr_view(request):
    return render(request, 'ajax01/01_demo01.html')


def server02_view(request):
    return HttpResponse('这是server02的响应内容')


def ajaxget_view(request):
    return render(request, "ajax01/02_ajax_get.html", locals())


def get_params_view(request, ):
    return render(request, "ajax01/03_get_params.html", locals())


def server03_view(request):
    # 接收前段传来的两个参数
    name = request.GET['uname']
    age = request.GET['uage']
    # 响应数据给前端
    s = "姓名:%s   年龄:%s" % (name, age)
    return HttpResponse(s)


def reg_view(request):
    return render(request, 'ajax01/04_.html')


def checkuname_view(request):
    # 1,接收前段传来的信息
    uname = request.GET['uname']
    users = models.Users.objects.filter(uname=uname)
    if users:
        return HttpResponse('1')
    return HttpResponse('0')


def add_view(request):
    uname = request.GET['uname']
    upwd = request.GET.get('upwd', '')
    print(upwd)
    uemail = request.GET.get('uemail', '')
    nickname = request.GET.get('nickname', '')
    try:
        models.Users.objects.create(
            uname=uname,
            upwd=upwd,
            uemail=uemail,
            nickname=nickname
        )
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse("0")


def post_view(request):
    return render(request, 'ajax01/05_post_reg.html', locals())


def post_data_view(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    uemail = request.POST['uemail']
    nickname = request.POST['nickname']
    try:
        models.Users.objects.create(
            uname=uname,
            upwd=upwd,
            uemail=uemail,
            nickname=nickname
        )
    except Exception as e:
        print(e)
        return HttpResponse("0")
    return HttpResponse("1")


def display_view(request):
    return render(request, 'ajax01/06_display.html')


def display_data_view(request):
    users = models.Users.objects.all()
    msg = ''
    for u in users:
        msg += "%s_%s_%s_%s_%s|" % (u.id, u.uname, u.upwd, u.uemail, u.nickname)
    msg = msg[0:-1]
    return HttpResponse(msg)


def json_js_view(request):
    return render(request, "ajax01/07_json_js.html")


def jsonserver_view(request):
    # 使用字典表示为JSON字符串
    dic = {
        'course': 'AJAX',
        'duration': 3,
        'place': 'bj'
    }

    # 1.将dic通过JSON.dumps方法转换为JSON字符串
    json_str = json.dumps(dic)

    # 2.使用列表表示多个JSON数据
    arr = [
        {'course': 'AJAX', 'duration': 3, 'place': 'bj'},
        {'course': 'Django', 'duration': 8, 'place': 'aj'},
        {'course': 'Jquery', 'duration': 5, 'place': 'cj'},
        {'course': 'CSS', 'duration': 2, 'place': 'dj'}

    ]
    json_str1 = json.dumps(arr)

    return HttpResponse(json_str1)


def serve08_view(request):
    users = models.Users.objects.all()
    json_str = serializers.serialize('json', users)
    return HttpResponse(json_str)


def display1_view(request):
    return render(request, 'ajax01/08_json_display.html')


def js_json_view(request):
    return render(request, 'ajax01/09_js_json.html', locals())


def server09_view(request):
    str = '{"uname": "wangwc", "uage": 30, "ugender": "unknow"}'
    dic = json.loads(str)
    s = "姓名:%s  年龄:%s  性别:%s" % (dic['uname'], dic['uage'], dic['ugender'])
    return HttpResponse(s)


def json_reg_view(request):
    return render(request, 'ajax01/10_reg.html', locals())


def server10_view(request):
    str = request.GET['str']
    dic = json.loads(str)
    try:
        models.Users.objects.create(
            uname=dic['uname'],
            upwd=dic['upwd'],
            uemail=dic['uemail'],
            nickname=dic['nickname']
        )
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse("0")


def head_view(request):
    return render(request, 'ajax01/11_head.html', locals())


def index_view(request):
    return render(request, "ajax01/11_index.html", locals())


def jq_get_view(request):
    return render(request, "ajax01/12_jq_get.html", locals())


def search_view(request):
    return render(request, "ajax01/13_search.html", locals())


def server13_view(request):
    # //接收前端传来的参数  kw
    # //查询users实体类中包含 kw 的信息
    # //将uname封装成列表,转换为JSON字符串
    # kw = request.GET['kw']
    users = models.Users.objects.filter(uname__contains = "王")
    ulist = []
    if users:
        for u in users:
            ulist.append(u.uname)
    return HttpResponse(json.dumps(ulist))


def ajax_view(request):
    return render(request,'ajax01/14_ajax.html',locals())