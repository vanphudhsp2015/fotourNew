# Generated by Django 2.1 on 2018-10-09 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20181003_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_place',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 21, 57, 7, 735846)),
        ),
    ]
