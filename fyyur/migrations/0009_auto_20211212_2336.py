# Generated by Django 3.2.9 on 2021-12-12 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyyur', '0008_auto_20211212_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='artist',
            new_name='artist_id',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='venue',
            new_name='venue_id',
        ),
    ]
