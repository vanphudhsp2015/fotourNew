# Generated by Django 2.1 on 2018-11-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourer', '0011_auto_20181009_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourer',
            name='id',
            field=models.AutoField(auto_created=True, default=1991, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourer',
            name='email',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
