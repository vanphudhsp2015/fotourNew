# Generated by Django 2.1.4 on 2018-12-26 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0074_auto_20181226_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 9, 25, 45, 379953)),
        ),
    ]
