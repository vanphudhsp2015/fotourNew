# Generated by Django 2.1 on 2018-12-07 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0029_auto_20181207_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentplace',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 40, 9, 659319)),
        ),
    ]
