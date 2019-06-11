from django.shortcuts import render, get_object_or_404
from map.models import Group, Country


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
            else:
                if(search_category == "country"):
                 groups = Group.objects.filter(country=value)
    return render (request,'search.html', {'groups': groups},)


def map(request):

        country = Country.objects.all()
        return render (request,'map.html', {'country': country})

def contr(request):
    search_category = request.GET.get('q', None)
    c = Country.objects.filter(namec=search_category)
    return render (request,'c.html', {'c': c},)

def r(request):
    return render (request,'r.html')
