# Generated by Django 4.2.7 on 2024-01-26 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
