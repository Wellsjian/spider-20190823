from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def page01_view(request):
    return HttpResponse("music/page01页")
def page02_view(request):
    return HttpResponse("music/page02页")
def page03_view(request):
    return HttpResponse("music/page03页")
