# Generated by Django 2.1 on 2018-11-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20181122_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placetour',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
