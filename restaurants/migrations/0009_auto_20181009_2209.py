# Generated by Django 2.1 on 2018-10-09 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20181009_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 772509)),
        ),
    ]
