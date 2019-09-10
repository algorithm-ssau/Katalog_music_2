from django.db import models

class Year(models.Model):
    year = models.IntegerField(verbose_name='Год')

    def __str__(self):
        return str(self.year)

class Group(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, verbose_name='Название группы')
    description = models.TextField(verbose_name='Описание группы')
    image = models.URLField(max_length=300,verbose_name='Ссылка на фото группы', default='')

    def __str__(self):
        return self.name

class Album(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, verbose_name='Название альбома')
    description = models.TextField(verbose_name='Описание альбома')
    image = models.URLField(max_length=300,verbose_name='Ссылка на изображение альбома', default='')

    def __str__(self):
        return self.name
