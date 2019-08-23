from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . import models


# Create your views here.
def index_view(request):
    return render(request, "user/index.html", locals())


def login_view(request):
    # 判断session里有没有存储该用户的密码
    value = request.session.get("mypasswd", '没有设置密码')
    if request.method == "GET":
        # 判断cokkies里是否存在
        username = request.COOKIES.get('username', '')
        return render(request, "user/login.html", locals())
    elif request.method == "POST":
        username = request.POST.get("username", '')
        if not username:
            user_error = '用户名不为空'
            return render(request, 'user/login.html', locals())
        password = request.POST.get("password")
        if not password:
            pass_error = "密码不能为空"
            return render(request, 'user/login.html', locals())
        # 将passwd 存储在 session中
        request.session["mypasswd"] = password
        try:
            user = models.User.objects.get(
                username=username,
                password=password
            )
        except:
            pass_error = "用户名或密码不正确!!!"
            return render(request, 'user/login.html', locals())
        # 在session中标记用户是登录状态
        request.session['user'] = {
            'username': user.username,
            'id': user.id
        }
        rem = request.POST.get("rem")
        rest = HttpResponseRedirect("/mynote/add")
        if rem == "1":
            rest.set_cookie("username", username)
        else:
            rest.delete_cookie("username")
        return rest


def reg_view(request):
    if request.method == "GET":
        # 判断cokkies里是否存在
        username = request.COOKIES.get('username', '')
        return render(request, "user/reg.html", locals())
    elif request.method == "POST":
        username = request.POST.get("username", '')
        if not username:
            user_error = '用户名不为空'
            return render(request, 'user/reg.html', locals())
        try:
            res = models.User.objects.get(username=username)
            if res:
                user_error = '用户名已经存在'
                return render(request, 'user/reg.html', locals())
        except:
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            if password != password1:
                pass_error = "两次密码不一样"
                return render(request, 'user/login.html', locals())
            models.User.objects.create(
                username=username,
                password=password
            )
            return HttpResponseRedirect('/user/login')


from . import forms


def reg2_view(request):
    if request.method == "GET":
        reg2 = forms.Reg2

        return render(request, 'user/reg2.html', locals())
    elif request.method == 'POST':
        # 方法一    通过request.POST
        form = forms.Reg2(request.POST)
        # 表单验证
        if form.is_valid():
            html = str(form.cleaned_data)
            return HttpResponse(html)
        else:
            return HttpResponse("您的提交不合法")


def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
        return HttpResponseRedirect("/user/")
    else:
        return HttpResponseRedirect("login")
