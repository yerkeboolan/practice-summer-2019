# Generated by Django 2.2.2 on 2019-07-26 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentProgress', '0002_auto_20190725_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentattendance',
            options={'ordering': ('pk',)},
        ),
    ]
