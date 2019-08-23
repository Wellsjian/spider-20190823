from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page01$',views.show_page_view),
    url(r'^add$',views.add_book_view),
    url(r'^add2$',views.books_add2_view),
    url(r'^books',views.books_view),
]