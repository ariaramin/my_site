# Generated by Django 3.1.6 on 2021-03-09 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210307_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='session',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]
