# Generated by Django 3.1.7 on 2021-06-14 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_is_instructor'),
        ('course', '0015_remove_course_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.account'),
        ),
    ]
