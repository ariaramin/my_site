# Generated by Django 3.1.6 on 2021-02-25 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('session', '0001_initial'),
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='session',
            field=models.ManyToManyField(to='session.Session'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='Student', to=settings.AUTH_USER_MODEL),
        ),
    ]
