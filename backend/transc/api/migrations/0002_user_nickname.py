# Generated by Django 4.2.7 on 2024-01-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
