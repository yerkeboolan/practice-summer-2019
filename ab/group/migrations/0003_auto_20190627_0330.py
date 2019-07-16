# Generated by Django 2.2.2 on 2019-06-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20190613_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject_id', models.IntegerField()),
                ('teacher_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]