# Generated by Django 2.1 on 2018-09-26 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20180926_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 20, 9, 4, 86653)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 20, 9, 4, 87653)),
        ),
    ]
