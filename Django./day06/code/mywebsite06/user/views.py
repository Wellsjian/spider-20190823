from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def login_view(request):
    value = request.session.get('mypassword', '没有设置密码')
    print('密码是:', value)
    if request.method == 'GET':
        username = request.COOKIES.get('myname', '')
        return render(request, 'user/login.html', locals())
    elif request.method == "POST":
        username = request.POST.get('username', '')
        if not username:
            name_error = "请填写用户名!!!"
            return render(request, 'user/login.html', locals())
        password = request.POST.get('password', '')
        if not password:
            password_error = "请填写用户密码!!!"
            return render(request, 'user/login.html', locals())
        # 将用户密码存储在session中
        request.session['mypassword'] = password
        # 进行登录逻辑操作
        try:
            auser = models.User.objects.get(
                username=username,
                password=password
            )
        except:
            password_error = "用户名或密码不正确!!!"
            return render(request, 'user/login.html', locals())
        # 如果走到此处用户密码正确
        # 在sssion中标记用户是登录状态
        request.session['user'] = {
            'name': auser.username,
            'id': auser.id
        }
        remember = request.POST.get('remember', '')
        resp = HttpResponse("提交成功:remember = " + remember)
        if remember == "1":
            resp.set_cookie('myname', username)
        else:
            resp.delete_cookie("myname")
        return resp


def logout_view(request):
    # 退出登录
    if 'user' in request.session:
        del request.session['user']
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("/    ")


def reg_view(request):
    if request.method == "GET":
        return render(request, 'user/reg.html')
    elif request.method == "POST":
        username = request.POST.get('username', '')
        if not username:
            name_error = "请输入用户名"
            return render(request, "user/reg.html", locals())
        try:
            a_user = models.User.objects.get(username=username)
            name_error = "用户名已经存在"
            return render(request, "user/reg.html", locals())
        except:
            password = request.POST.get('password', '')
            if not password:
                passeord_error = "请输入用户密码"
            password1 = request.POST.get('password1', '')
            if not password:
                passeord1_error = "请输入用户密码"

            if password != password1:
                passeord1_error = "两次密码不一致"

            user = models.User.objects.create(
                username=username,
                password=password
            )
            html = username + '注册成功 <a href="/user/login">返回登录'
            return HttpResponse(html)
