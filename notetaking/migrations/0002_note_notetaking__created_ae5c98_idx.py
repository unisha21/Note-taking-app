# Generated by Django 5.0.1 on 2024-01-30 09:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notetaking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['created_at'], name='notetaking__created_ae5c98_idx'),
        ),
    ]
