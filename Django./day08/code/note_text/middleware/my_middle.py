
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re

class MyMiddleware(MiddlewareMixin):
    #自定义一个MiddlewareMixin类
    #记录该网站的访问次数
    count = 0
    def process_request(self,request):
        self.__class__.count += 1
        print('count = ',self.__class__.count)
        if self.__class__.count <= 5:
            return None
        return HttpResponse("2222222222222222222222222222222222")

class LimitVisit(MiddlewareMixin):
    visit_times = {} #键是IP地址,值是访问次数
    def process_request(self,request):
        if request.method != "POST":
            return None
        ip = request.META['REMOTE_ADDR']
        if not re.match(r"/user/reg",request.path_info):
            return
        times = self.visit_times.get(ip,0)
        self.visit_times[ip] = times + 1
        print(self.visit_times)
        if times > 2 :
            return HttpResponse("你已经被拒绝注册")

