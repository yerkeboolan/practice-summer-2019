# Generated by Django 2.2.2 on 2019-07-25 10:32

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
            name='GroupAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='group.Group')),
            ],
        ),
        migrations.CreateModel(
            name='QuizHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('theory', models.IntegerField()),
                ('practice', models.IntegerField()),
                ('topic_id', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RealTestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('subject_id', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att', models.BooleanField()),
                ('rating', models.FloatField()),
                ('group_att', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_att', to='studentProgress.GroupAttendance')),
                ('group_student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='group.GroupStudent')),
            ],
        ),
        migrations.CreateModel(
            name='RealTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userInfo.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='QuizRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('theory', models.IntegerField()),
                ('practice', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_quiz', to='userInfo.Student')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.Topic')),
            ],
        ),
    ]
