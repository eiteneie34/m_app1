# Generated by Django 3.2.5 on 2021-12-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw_visual', '0013_alter_rwvisual_dot_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rwvisual',
            name='dot_marker',
            field=models.CharField(choices=[('.', 'Punkt'), ('o', 'Kreis'), ('s', 'Quadrat'), ('^', 'Dreieck ^'), ('v', 'Dreieck v'), ('8', 'Octagon'), ('D', 'Diamant'), ('d', 'Rombe'), ('p', 'Pentagon'), ('H', 'Hexagon'), ('(4,1)', 'Stern 4'), ('*', 'Stern 5'), ('(7,1)', 'Stern 7'), ('(8,1)', 'Stern 8'), ('(9,1)', 'Stern 9'), ('(5,2)', 'Schneeflocke 5'), ('(6,2)', 'Schneeflocke 6'), ('(7,2)', 'Schneeflocke 7'), ('(8,2)', 'Schneeflocke 8'), ('(9,2)', 'Schneeflocke 9')], default='.', max_length=10),
        ),
    ]
