# Generated by Django 5.1.6 on 2025-03-08 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='formmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('datecreated', models.DateTimeField(default=datetime.datetime(2025, 3, 8, 9, 15, 37, 910439, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
