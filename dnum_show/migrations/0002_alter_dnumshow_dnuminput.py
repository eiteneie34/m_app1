# Generated by Django 3.2.5 on 2021-10-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnum_show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnumshow',
            name='dnumInput',
            field=models.CharField(default='0,0001', max_length=50),
        ),
    ]
