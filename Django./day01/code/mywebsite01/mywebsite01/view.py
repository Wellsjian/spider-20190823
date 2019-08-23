from django.http import HttpResponse


def pagel_view(request):
    html = "欢迎来到第一个网页,这里会告诉你一些需要注意的事项"
    html += '<a href="http://www.tmooc.cn">达内</a>'
    html += '<a href="/page2">第二页</a>'
    return HttpResponse(html)


def index_view(request):
    html = "欢迎来到小建之家"
    html += '<a href="/page1">第一页</a>'
    html += '<a href="/page2">第二页</a>'
    # html =  '<img src="./happy.gif" alt="">'
    return HttpResponse(html)


def page2_view(request):
    html = "这里是第二页,这里是我们即将开始的路程,加油吧"
    html += '<a href="/">首页</a>'
    html += '<a href="/page1">第一页</a>'
    # html =  '<img src="./happy.gif" alt="">'
    return HttpResponse(html)


# 带有参数的视图函数传参http://127.0.0.1:22222/year/2222 返回的是URL中的年份是2222
def year_view(request, year):
    html = "URL中的年份是" + year
    return HttpResponse(html)


def option_view(request, num1, option, num2):
    if option == "add":
        res = int(num1) + int(num2)
    elif option == "sub":
        res = int(num1) - int(num2)
    elif option == "mul":
        res = int(num1) * int(num2)
    else:
        res = "不能运算"
    return HttpResponse("结果是" + str(res))


def date_view(request, year, month, day):
    html = year + "年" + month + "月" + day + "日"
    return HttpResponse(html)


def show_info_view(request):
    html = request.path
    if request.method == "GET":
        html += "<h2>您正在进行GET请求</h2>"
    elif request.method == "POST":
        html += "<h2>您正在进行GET请求</h2>"
    html += "<h2>您的IP地址为:</h2>" + request.META['REMOTE_ADDR']
    html += "<h2>您的IP地址为:</h2>" + request.META['HTTP_REFERER']
    return HttpResponse(html)

#通过get方法来获取数据值
def page_view(request):
    html = ""
    if request.method == "GET":
        dic = str(dict(request.GET))
        html += "GET请求" + dic
        html += '<br>' + "b =" + str(request.GET.get("b","没有值"))
        html += '<br>' + "a =" + str(request.GET.getlist("a"))
    elif request.method == "POST":
        pass
    return HttpResponse(html)

def sum_view(request):
    html = ""
    if request.method == "GET":
        start = request.GET.get('start')
        if not start:
            start = 0
        stop = int(request.GET.get('stop'))
        step = int(request.GET.get('step'))
        html += str(sum(range(int(start),stop,step)))

        return HttpResponse(html)

def get1_view(request):
    if request.method == "GET":
        return HttpResponse(str(request.environ).lower())











