# Generated by Django 2.2.2 on 2019-07-28 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentProgress', '0005_auto_20190728_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentattendancehistory',
            old_name='group_att',
            new_name='group_att_id',
        ),
        migrations.RenameField(
            model_name='studentattendancehistory',
            old_name='group_student',
            new_name='group_student_id',
        ),
    ]
