from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
    # return HttpResponse('index:index')
    return render(request,'show_image.html',locals())