# Generated by Django 3.2.5 on 2021-11-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw_visual', '0007_auto_20211108_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rwvisual',
            name='dot_cmap',
            field=models.CharField(choices=[('n', 'kein Farbverlauf'), ('tab10', 'tab10'), ('tab20', 'tab20'), ('tab20b', 'tab20b'), ('tab20c', 'tab20c'), ('Greys', 'Greys'), ('Greens', 'Greens'), ('Blues', 'Blues'), ('Purples', 'Purples'), ('Reds', 'Reds'), ('Oranges', 'Oranges'), ('Wistia', 'Wistia'), ('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter')], default='Purples', max_length=100),
        ),
    ]
