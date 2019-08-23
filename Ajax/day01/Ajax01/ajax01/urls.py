from django.conf.urls import url
from . import views


urlpatterns = [
    #演示创建XHR
    url(r'^01_createxhr/$',views.createXhr_view),
    #演示使用AJAX发送get请求的步骤
    url(r'^02_server/$',views.server02_view),
    url(r'^02_ajax_get/$',views.ajaxget_view),
    #演示使用ajax发送get请求并附有参数
    url(r'^03_ajax_get_params/',views.get_params_view),
    url(r'^03_server/',views.server03_view),
    url(r"^04_reg/",views.reg_view),
    url(r"^04_server/",views.checkuname_view),
    url(r"^04_server02/",views.add_view),
    url(r"^05_server/",views.post_data_view),
    url(r"^05_post/",views.post_view),
    url(r"^06_display/",views.display_view),
    url(r"^06_server/",views.display_data_view),
    #在前端中解析JSON字符串
    url(r"^07_json_js/",views.json_js_view),
    #在服务器端中将数据打包成JSON字符串
    url(r"^07_jsonserver/",views.serve08_view),
    # 在服务器端中将数据库中元转换为字符串
    url(r"^08_jsonuser/",views.serve08_view),
    url(r"^08_server/",views.serve08_view),
    url(r"^08_display/",views.display1_view),
    #在前端中将JS对象转化为JSON字符串
    url(r"^09_js_json/",views.js_json_view),
    url(r"^09_server/",views.server09_view),
    #通过JSON完成注册操作
    url(r"^10_server/",views.server10_view),
    url(r"^10_json_reg/",views.json_reg_view),
    #演示JQ中的$obj.load()的作用
    url(r"11_head",views.head_view),
    url(r"11_index",views.index_view),
    url(r"12_jq_get",views.jq_get_view),
    url(r"13_search/",views.search_view),
    url(r"^13_server/",views.server13_view),
    #通过$.ajax完成自定义的ajax请求
    url(r"^14_ajax/",views.ajax_view),

]
