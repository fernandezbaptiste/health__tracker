# Generated by Django 3.1 on 2023-08-22 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230821_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='consume',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]