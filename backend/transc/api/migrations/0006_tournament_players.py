# Generated by Django 4.2.7 on 2024-02-06 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_game_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='joined_tournaments', to=settings.AUTH_USER_MODEL),
        ),
    ]