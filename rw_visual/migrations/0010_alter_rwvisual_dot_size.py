# Generated by Django 3.2.5 on 2021-11-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw_visual', '0009_auto_20211114_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rwvisual',
            name='dot_size',
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('250', '250'), ('500', '500'), ('750', '750'), ('1000', '1000'), ('2500', '2500'), ('5000', '5000'), ('7500', '7500'), ('10000', '10000')], default='5.0', max_length=10),
        ),
    ]
