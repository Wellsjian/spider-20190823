
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r"^$",views.index_view),
    url(r"^add$",views.add_books_view),
    url(r"^display$",views.display_books_view),
    url(r"^add_finally$",views.add_finally),
    url(r"^mod/(\d+)$",views.mod_view),
    url(r"^del/(\d+)$",views.del_view),
    url(r"^select$",views.select_view),
]