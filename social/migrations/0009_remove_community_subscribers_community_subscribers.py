# Generated by Django 5.1.1 on 2024-11-19 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_community_subscribers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='community',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='sucribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
