# Generated by Django 3.0.4 on 2020-11-06 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20201105_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='mail_id',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='officer',
            old_name='mail_id',
            new_name='mail',
        ),
    ]
