# Generated by Django 2.1 on 2018-12-07 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0056_auto_20181127_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 34, 50, 368220)),
        ),
    ]
