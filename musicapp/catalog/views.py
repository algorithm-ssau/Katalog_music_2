from django.shortcuts import render
from catalog.models import Year, Group, Album

def catalog(request):
    years = Year.objects.all()
    return render(request, 'catalog.html', {'years': years})

def groups(request, year):
    groups = Group.objects.filter(year__year=year)
    return render(request, 'groups.html', {'groups': groups})

def albums(request, group_name):
    albums = Album.objects.filter(group__name=group_name)
    return render(request, 'albums.html', {'albums': albums})
