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

    def __str__(self):
        return self.name
