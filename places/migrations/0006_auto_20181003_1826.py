# Generated by Django 2.1 on 2018-10-03 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20180927_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_place',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 18, 26, 2, 458443)),
        ),
    ]
