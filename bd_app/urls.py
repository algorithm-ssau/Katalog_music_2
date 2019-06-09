from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from bd_app.models import Groap

urlpatterns = [
    url(r'^$',
    ListView.as_view( queryset=Groap.objects.all(),
    template_name="bd_app/post.html" )),
    ]




'''from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]'''
