# Generated by Django 2.1 on 2018-11-22 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0029_auto_20181122_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 22, 18, 17, 5, 341350)),
        ),
    ]
