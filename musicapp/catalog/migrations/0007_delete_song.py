# Generated by Django 2.2 on 2019-09-10 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Song',
        ),
    ]