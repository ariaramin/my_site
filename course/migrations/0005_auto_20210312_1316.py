# Generated by Django 3.1.6 on 2021-03-12 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_course'),
        ('course', '0004_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
