# Generated by Django 2.2.2 on 2019-06-27 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20190627_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_group', to='userInfo.Student'),
        ),
    ]