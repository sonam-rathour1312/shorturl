# Generated by Django 3.2.4 on 2021-06-22 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url',
            new_name='long_url',
        ),
    ]
