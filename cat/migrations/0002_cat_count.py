# Generated by Django 2.2.6 on 2020-06-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
