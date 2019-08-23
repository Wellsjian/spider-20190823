from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.

# 主页
def index_view(request):
    # if request.method == "GET":
    # return  HttpResponse("好啊")
    return render(request, "bookstore/index.html")


def add_books_view(request):
    return render(request, 'bookstore/add_books.html')


def display_books_view(request):
    books = models.Book.objects.all()
    return render(request, 'bookstore/display.html', locals())


def add_finally(request):
    if request.method == "GET":
        return render(request, 'bookstore/display.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        pub_house = request.POST.get("pub_house")
        price = request.POST.get("price")
        market_price = request.POST.get("market_price")
        try:
            abook = models.Book.objects.create(
                title=title,
                pub_house=pub_house,
                price=price,
                market_price=market_price

            )
            return HttpResponseRedirect("/my_bookstore/display")
        except:
            return HttpResponse('添加失败')


def mod_view(request, id_name):
    abook = models.Book.objects.get(id=id_name)
    if request.method == "GET":

        return render(request, 'bookstore/mod_books.html', locals())
    elif request.method == "POST":
        try:
            abook.pub_house = request.POST.get("pub_house")
            abook.price = request.POST.get("price")
            abook.market_price = request.POST.get("market_price")
            abook.save()
            return HttpResponseRedirect("/my_bookstore/display")
        except:
            return HttpResponse('修改失败')


def del_view(request, id_name):
    try:
        abook = models.Book.objects.get(id=id_name)
        abook.delete()
        return HttpResponseRedirect("/my_bookstore/display")
    except:
        return HttpResponse("删除失败")


def select_view(request):
    if request.method == "GET":
        return render(request, "bookstore/select.html")
    elif request.method == "POST":
        price = request.POST.get("select")

        abook = models.Book.objects.filter( market_price__gt=price)
        return render(request,"bookstore/select.html",locals())

