# Generated by Django 4.2.11 on 2024-03-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]
