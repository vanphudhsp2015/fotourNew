# Generated by Django 2.1 on 2018-11-23 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0024_auto_20181123_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 42, 11, 242688)),
        ),
        migrations.AlterField(
            model_name='taskspeak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 42, 11, 243688)),
        ),
    ]