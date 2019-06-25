# Generated by Django 2.2.2 on 2019-06-25 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20190619_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtopic', to='subject.Topic'),
        ),
    ]
