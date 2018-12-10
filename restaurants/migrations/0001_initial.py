# Generated by Django 2.1 on 2018-09-25 01:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourer', '0007_remove_tourer_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commnet', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 25, 8, 54, 50, 192644))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourer.Tourer')),
            ],
        ),
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_food', models.CharField(max_length=250)),
                ('info_food', models.CharField(max_length=250)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('img_status', models.FileField(default='/default/user-avatar-default-165.png', upload_to='restaurant/book/')),
            ],
        ),
        migrations.CreateModel(
            name='Eating_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('start_status', models.CharField(max_length=5000)),
                ('end_status', models.CharField(max_length=5000)),
                ('img_status', models.FileField(default='/default/user-avatar-default-165.png', upload_to='house/book/')),
                ('eating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Eating')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restaurant', models.CharField(max_length=250)),
                ('type_restaurant', models.CharField(max_length=250)),
                ('image_restaurant', models.FileField(default='/default/user-avatar-default-165.png', upload_to='restaurant/')),
                ('review', models.IntegerField(default=0)),
                ('star', models.FloatField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.City')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 25, 8, 54, 50, 192644))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourer.Tourer')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='eating',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='comment_restaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
    ]
