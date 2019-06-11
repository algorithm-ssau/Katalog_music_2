from django.db import models


class Group(models.Model):
    name = models.CharField("Название Группы", max_length=200, default="")
    country = models.CharField("Страна", max_length=200, default="")
    style= models.CharField("Жанр", max_length=30, default="")
    age = models.IntegerField("Год деятельности", default=1950)
    songs = models.TextField("Песни", default="")
    sostav= models.TextField("Состав группы", default="")
    alboms = models.TextField("Альбомы", default="")
    history =  models.TextField("История группы", default="")

class Country(models.Model):

    namec = models.CharField("Название Страны", max_length=200, default="")
    countryo = models.TextField("Краткое описание страны", max_length=200, default="")
    countryop= models.TextField("Описание страны", max_length=100000, default="")



def __str__(self):
        return self.name
