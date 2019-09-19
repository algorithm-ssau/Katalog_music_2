from django.shortcuts import render
from catalog.models import Director, Film

def main(request):
    return render(request, 'main.html', {})

def catalog(request):
    directors = Director.objects.all()
    return render(request, 'catalog.html', {'directors': directors})

def films(request, director):
    films = Film.objects.filter(director__name=director)
    return render(request, 'groups.html', {'films': films})


