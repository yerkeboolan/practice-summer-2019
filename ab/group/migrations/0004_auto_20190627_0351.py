# Generated by Django 2.2.2 on 2019-06-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20190627_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupStudentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]