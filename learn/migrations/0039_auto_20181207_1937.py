# Generated by Django 2.1 on 2018-12-07 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0038_auto_20181207_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 37, 33, 468029)),
        ),
        migrations.AlterField(
            model_name='taskspeak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 37, 33, 468029)),
        ),
    ]
