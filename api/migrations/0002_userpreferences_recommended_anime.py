# Generated by Django 4.2.17 on 2024-12-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='recommended_anime',
            field=models.ManyToManyField(blank=True, related_name='recommended_for', to='api.anime'),
        ),
    ]