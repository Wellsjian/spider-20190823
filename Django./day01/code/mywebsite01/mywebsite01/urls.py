"""mywebsite01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view #包的相对路径导入模块


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^page',view.page_view),
    url(r'^sum',view.sum_view),
    url(r'^get$',view.get1_view),
    url(r'^show_info$',view.show_info_view),
    url(r'^page1$', view.pagel_view),
    url(r'^$', view.index_view),
    url(r'^page2$', view.page2_view),
    url(r'^year/(\d{4})$',view.year_view),
    url(r'^(\d+)/(\w+)/(\d+)$',view.option_view),
    url(r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$',view.date_view)
]
