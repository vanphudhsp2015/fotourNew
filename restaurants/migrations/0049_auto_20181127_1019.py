# Generated by Django 2.1 on 2018-11-27 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0048_auto_20181127_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 27, 10, 19, 22, 304040)),
        ),
    ]
