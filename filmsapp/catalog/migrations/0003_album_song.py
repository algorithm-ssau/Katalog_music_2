# Generated by Django 2.2 on 2019-09-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название альбома')),
                ('description', models.TextField(verbose_name='Описание альбома')),
                ('image', models.URLField(default='', max_length=300, verbose_name='Ссылка на изображение альбома')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название песни')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Album')),
            ],
        ),
    ]
