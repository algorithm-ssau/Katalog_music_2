# Generated by Django 2.2 on 2019-09-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_delete_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(verbose_name='Год'),
        ),
    ]
