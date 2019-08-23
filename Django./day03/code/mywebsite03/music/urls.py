

from django.conf.urls import url
from . import views

urlpatterns = [
    #路由为music/page1
    url(r"^page1$",views.page01_view),
    url(r"^page2$",views.page02_view),
    url(r"^page3$",views.page03_view),
]







