from django.shortcuts import render

def index(request):
    return render (request,'bd_app/post.html')
