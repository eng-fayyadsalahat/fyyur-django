# Generated by Django 3.2.9 on 2021-12-06 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyyur', '0002_auto_20211206_2235'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='artist',
            table='Artist',
        ),
        migrations.AlterModelTable(
            name='show',
            table='Show',
        ),
        migrations.AlterModelTable(
            name='venue',
            table='Venue',
        ),
    ]
