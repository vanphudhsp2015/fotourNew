# Generated by Django 2.1 on 2018-11-23 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0027_auto_20181123_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 14, 52, 256277)),
        ),
    ]
