# Generated by Django 5.1.1 on 2024-12-14 07:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KidStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('GOOD', 'Good Kid'), ('NAUGHTY', 'Naughty Kid')], default='GOOD', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kid_statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]