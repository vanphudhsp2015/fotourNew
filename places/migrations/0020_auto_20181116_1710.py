# Generated by Django 2.1 on 2018-11-16 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_auto_20181116_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_place',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 17, 10, 17, 187334)),
        ),
    ]
