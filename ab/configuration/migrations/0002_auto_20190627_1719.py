# Generated by Django 2.2.2 on 2019-06-27 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userstatusconfig',
            options={'ordering': ['id', 'status']},
        ),
    ]
