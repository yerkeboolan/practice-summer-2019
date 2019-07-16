# Generated by Django 2.2.2 on 2019-06-25 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20190625_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_quiz', models.BooleanField()),
                ('created_date', models.DateTimeField()),
                ('origin_id', models.IntegerField()),
                ('subject_id', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topic', to='subject.Subject'),
        ),
    ]