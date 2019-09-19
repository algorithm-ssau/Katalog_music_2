from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=40,verbose_name='Имя режиссера')
    description = models.TextField(verbose_name='Описание режиссера')
    image = models.URLField(max_length=300,verbose_name='Ссылка на фото режиссера', default='')

    def __str__(self):
        return str(self.name)

class Film(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фиьма')
    trailer = models.URLField(max_length=300,verbose_name='Ссылка на трейлер фильма', default='')

    def __str__(self):
        return self.name

