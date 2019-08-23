from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from user import models as u_models
from django.core.paginator import Paginator as p
from django.conf import settings
import os


# Create your views here.

# 函数装饰器来判断用户是否登录
def check_login(fun):
    def wrap(request, *args, **kwargs):
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        else:
            return fun(request, *args, **kwargs)

    return wrap


@check_login
def add_view(request):
    # 判断用户是否登录
    # if 'user' not in request.session:
    #     return HttpResponseRedirect('/user/login')
    if request.method == "GET":
        return render(request, 'mynote/add_note.html')
    elif request.method == "POST":
        title = request.POST.get('title', '')
        # 根据登录用户的id找到用户
        try:
            a_user = u_models.User.objects.get(id=request.session['user']['id'])
        except:
            return HttpResponseRedirect('/user/reg')
        content = request.POST.get('content', '')
        # 根据获取内容连接数据库并储存
        models.Note.objects.create(
            title=title,
            content=content,
            user=a_user
        )
        return HttpResponseRedirect('/mynote/')


@check_login
def list_view(request):
    try:
        a_user_id = request.session['user']['id']
        # a_user = request.session['user']['username']
        a_user = u_models.User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    notes = a_user.note_set.all()
    # return render(request,'mynote/list_note.html',locals())
    paginator = p(notes, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.page(int(page_number))
    return render(request, 'mynote/list_note2.html', locals())


@check_login
def mod_view(request, id):
    try:
        a_user_id = request.session['user']['id']
        # a_user = request.session['user']['username']
        a_user = u_models.User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    a_note = models.Note.objects.get(id=id)
    if request.method == "GET":
        return render(request, "mynote/mod_note.html", locals())
    elif request.method == "POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        a_note.title = title
        a_note.content = content
        a_note.save()

    return HttpResponseRedirect('/mynote/')


@check_login
def del_view(request, id):
    try:
        a_user_id = request.session['user']['id']
        # a_user = request.session['user']['username']
        a_user = u_models.User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    a_note = models.Note.objects.get(id=id)
    a_note.delete()
    return HttpResponseRedirect('/mynote/')


def upload_view(request):
    if request.method == "GET":
        return render(request,'mynote/upload_file.html',locals())
    elif request.method == "POST":
        # filename = request.POST.get('myfile')
        # print(str(filename))
        #此时可以通过request.FILES来获取上传的文件
        a_file = request.FILES["myfile"]
        # 此处保存上传的文件到项目文件夹/static/files文件夹内
        filename = os.path.join(settings.MEDIA_ROOT ,a_file.name)
        with open(filename,'wb') as f:
            #a_file.file绑定一个已经打开的文件流对象
            data = a_file.file.read()
            f.write(data)
            return  HttpResponse('文件' + a_file.name + "上传成功")
        # return  HttpResponse('文件' + str(filename[0]) + "再次上传成功")

