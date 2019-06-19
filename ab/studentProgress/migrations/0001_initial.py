# Generated by Django 2.2.2 on 2019-06-13 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('subject', '0001_initial'),
        ('userInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInfo.Student')),
            ],
        ),
        migrations.CreateModel(
            name='RealTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInfo.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='QuizRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('theory', models.IntegerField()),
                ('practice', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInfo.Student')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att', models.BooleanField()),
                ('rating', models.FloatField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentProgress.Date')),
                ('group_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.GroupStudent')),
            ],
        ),
    ]