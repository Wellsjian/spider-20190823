from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def show_page_view(request):
    return HttpResponse('欢迎王者归来')


def add_book_view(request):
    if request.method == "GET":
        # btitle = request.GET.get('title', "No Name")
        # bpub_host = request.GET.get('pub_home', "清华大学出版社")
        # bpub_time = request.GET.get('pub_time', "")
        # 方法一
        # models.Book.objects.create(title=btitle, pub_time=bpub_time, pub_host=bpub_host)
        # 方法二
        book = models.Book()
        book.title = "Javascript"
        book.pub_host = "山东大学出版社"
        book.pub_time = "2019-01-15"
        book.save()
        print(book)
        return HttpResponse("添加成功")


def books_view(request):
    books = models.Book.objects.all()

    return render(request, 'bookstore/books.html', locals())
0

def books_add2_view(request):
    if request.method == "GET":
        return render(request, 'bookstore/booksinfo.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        pub_host = request.POST.get("pub_host")
        price = request.POST.get("price")
        pub_time = request.POST.get("pub_time")
        try:
            abook = models.Book.objects.create(
                title=title,
                pub_host=pub_host,
                price=price,
                pub_time=pub_time

            )
            return HttpResponseRedirect("/bookstore/books")
        except:
            return HttpResponse('添加失败')
