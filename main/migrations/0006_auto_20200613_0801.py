# Generated by Django 2.2.6 on 2020-06-13 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_set_nane'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='set_nane',
            new_name='set_name',
        ),
    ]
