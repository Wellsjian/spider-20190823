from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_view(request):
    return  HttpResponse('欢迎您回来')