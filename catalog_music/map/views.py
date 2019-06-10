from django.shortcuts import render, get_object_or_404
from map.models import Group

def home(request):
    return render (request, 'home.html')

def search(request):
    search_category = request.GET.get('q', None)
    value = request.GET.get('v', None)
    groups = 0
    if(search_category == "All"):
        groups = Group.objects.all()
        print("groups")
    else:
        if(search_category == "style"):
            groups = Group.objects.filter(style=value)
        else:
            if(search_category == "age"):
                groups = Group.objects.filter(age=value)
    return render (request,'search.html', {'groups': groups},)


def map(request):
    return render (request,'map.html')
def r(request):
    return render (request,'r.html')
