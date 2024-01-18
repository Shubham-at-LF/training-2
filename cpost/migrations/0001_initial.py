# Generated by Django 5.0.1 on 2024-01-18 06:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profilePic', models.CharField(max_length=400)),
                ('userSince', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='user_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpost.user')),
            ],
        ),
    ]
