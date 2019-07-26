# Generated by Django 2.2.2 on 2019-07-26 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjectContent', '0004_video'),
        ('access', '0002_auto_20190726_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoaccess',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subjectContent.Video'),
            preserve_default=False,
        ),
    ]
