# Generated by Django 2.2 on 2019-09-09 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название группы')),
                ('description', models.TextField(verbose_name='Описание группы')),
                ('image', models.URLField(default='', max_length=300, verbose_name='Ссылка на фото группы')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Year')),
            ],
        ),
    ]
