# Generated by Django 2.1 on 2018-10-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourer', '0008_tourer_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourer',
            name='id',
        ),
        migrations.AlterField(
            model_name='tourer',
            name='email',
            field=models.CharField(blank=True, max_length=250, primary_key=True, serialize=False),
        ),
    ]
