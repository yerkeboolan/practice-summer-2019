# Generated by Django 2.2.2 on 2019-07-25 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizConfigHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.IntegerField()),
                ('practice', models.BooleanField(default=False)),
                ('theory', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatusConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id', 'status'],
            },
        ),
        migrations.CreateModel(
            name='UserStatusConfigHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuizConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice', models.BooleanField(default=False)),
                ('theory', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.Subject')),
            ],
            options={
                'ordering': ['id', 'subject'],
            },
        ),
    ]
