# Generated by Django 2.2.2 on 2019-07-25 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20190725_1721'),
        ('studentProgress', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupattendance',
            unique_together={('date', 'group')},
        ),
    ]
