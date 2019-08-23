from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"set_cookies",views.set_cookies_view),
    url(r"get_cookies",views.get_cookies_view),
]