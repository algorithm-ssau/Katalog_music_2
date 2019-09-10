# Generated by Django 2.2 on 2019-09-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190910_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название песни')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Album')),
            ],
        ),
    ]