# Generated by Django 2.2 on 2019-09-09 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_album_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Song',
        ),
    ]
