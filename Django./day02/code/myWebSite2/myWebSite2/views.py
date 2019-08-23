
# file:mywebsite/views.py

from django.http import HttpResponse


def sum_view(request):
    """

    :type request: object
    """
    if request.method == "GET":
        start = request.GET.get('start',"0")
        stop = request.GET.get('stop')
        step = request.GET.get('step',"1")
        html = sum(range(int(start),int(stop),int(step)))
    return HttpResponse('结果是: %d' %html)

html = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/text_post" method="post">
        <input type="text" name="search_name">
        <select name="gender">
            <option value=1> 男</option>
            <option value=0> 女</option>
        </select>
        <textarea name="comment" rows="5" cols="10">附言</textarea>
        <input type="text" name="name2">
        <input type="submit" value="开始搜索">
    </form>

</body>
</html>    
    '''
def text_post_view(request):
    if request.method == "GET":
        return HttpResponse(html)
    elif request.method == "POST":
        value = request.POST["gender"]
        # dic = dict(request.POST)
        return HttpResponse("search_name" + value )
#第一种模板加载方式  通过 loader
# 第二种模板加载方式  通过   render

from django.template import loader
from django.shortcuts import render
def test1_view(request):
    person = {
        'name':'dog',
        'age':19,
        'color':'red'
    }
    # #绑定模板对象
    # t = loader.get_template("myhomepage.html")
    # # 生成HTML字符串
    # html = t.render()
    # return HttpResponse(html)
    return render(request,"myhomepage.html",person)

# 模板传参方式

def mysecondpage_view(request):
    myvar = 999
    mystr = 'Hello world'
    mylist = ['小建体育馆','小建牧场','小建农场']
    person = {'name':'xiaojian','age':25}
    def myfun1():
        return "函数结果"
    money = 999999
    cities = ['小建体育馆', '小建牧场', '小建农场','小建酒楼','小建广场']
    # cities = []
    return render(request,'mysecondpage.html',locals())



def page0_view(request):
    return render(request,"mybasepage.html")

def page1_view(request):
    return render(request,"mybasepage1.html")

def page2_view(request):
    return render(request,"mybasepage2.html")

def page3_view(request):
    return render(request, "page3.html")

def pagen_view(request,n):
    return render(request, "pagen.html",locals())

from django.shortcuts import render
def shebao_view(request):
    if request.method == 'GET':
        return render(request, 'shebao.html')
    elif request.method == "POST":
        value = int(request.POST.get('t_name'))
        c_name = request.POST.get('c_name')
        g_yanglao = value * 0.08
        c_yanglao = value * 0.19
        if int(c_name) == 0:
            g_shiye = 0
            c_shiye = value * 0.008
        elif int(c_name) == 1:
            g_shiye = value * 0.002
            c_shiye = value*0.008
        g_gongshang = 0
        c_gongshang = value * 0.005
        g_shengyu = 0
        c_shengyu = value * 0.008
        g_yiliao = 2 + value * 0.003
        c_yiliao = value * 0.1
        g_gongjijin = value * 0.12
        c_gongjijin = value * 0.12
        g_sum = g_yanglao + g_shiye + g_gongshang + g_shengyu + g_yiliao + g_gongjijin
        c_sum = c_yanglao + c_shiye + c_gongshang + c_shengyu + c_yiliao + c_gongjijin
        sum = g_sum + c_sum
        return render(request,"shebao.html",locals())


