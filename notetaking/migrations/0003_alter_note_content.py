# Generated by Django 5.0.1 on 2024-08-24 16:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notetaking', '0002_note_notetaking__created_ae5c98_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
