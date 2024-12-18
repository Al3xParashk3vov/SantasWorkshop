# Generated by Django 5.1.1 on 2024-12-18 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_presents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]