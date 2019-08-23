from django.conf.urls import url
from . import views

urlpatterns = [
    # 127.0.0.1:8000/v1/tokens
    url(r'^$', views.tokens_view, name='tokens')
]
