# Generated by Django 3.2.9 on 2021-12-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyyur', '0006_auto_20211212_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
