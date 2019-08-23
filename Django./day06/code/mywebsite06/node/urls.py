from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",views.index_view),
    url(r"^login$",views.login_view),
    url(r"^reg$",views.reg_view),
    url(r"^display$",views.display_view),
]