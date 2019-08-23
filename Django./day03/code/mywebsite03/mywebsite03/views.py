# file :mywebsite03/views

from django.shortcuts import render

def show_image_view(request):

    return render(request,"show_image.html",locals())