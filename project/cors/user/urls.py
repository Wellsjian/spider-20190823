from django.conf.urls import url
from . import views

urlpatterns = [
    # 127.0.0.1:8000/v1/users
    url(r'^$',views.users_view,name='users'),
    # 127.0.0.1:8000/v1/users/<username>
    url(r'^/(?P<username>[\w]+)$',views.users_view),
    #http://127.0.0.1:8000/v1/users/<username>/avatar
    url(r'^/(?P<username>[\w]+)/avatar$',views.avatar_view),

]