# Generated by Django 4.2.17 on 2024-12-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userpreferences_recommended_anime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreferences',
            name='recommended_anime',
        ),
    ]
