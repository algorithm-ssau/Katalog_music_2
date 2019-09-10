from django.shortcuts import render

def index(request):
    return render (request,'shablon_v1/home.html')
