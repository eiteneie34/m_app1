# Generated by Django 3.2.5 on 2021-10-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw_visual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rwvisual',
            name='video_n',
            field=models.FileField(blank=True, default='rwvisual/rw_visual_n', upload_to='rwvisual'),
        ),
        migrations.AddField(
            model_name='rwvisual',
            name='video_n2',
            field=models.FileField(blank=True, default='rwvisual/rw_visual_n2', upload_to='rwvisual'),
        ),
    ]
