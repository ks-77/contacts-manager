# Generated by Django 4.2 on 2024-10-23 22:55

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=20, validators=[common.validators.validate_phone_number])),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]