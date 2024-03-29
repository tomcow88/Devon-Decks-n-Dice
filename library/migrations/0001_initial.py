# Generated by Django 4.2.11 on 2024-03-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('bgg_id', models.IntegerField(unique=True)),
                ('year_published', models.IntegerField()),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('playing_time', models.IntegerField()),
                ('age', models.IntegerField()),
                ('image', models.URLField(unique=True)),
                ('thumbnail', models.URLField(unique=True)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=0)),
            ],
        ),
    ]
