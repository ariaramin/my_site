# Generated by Django 3.1.7 on 2021-06-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210519_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
