# Generated by Django 3.1.6 on 2021-03-05 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
