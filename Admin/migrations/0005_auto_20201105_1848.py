# Generated by Django 3.0.4 on 2020-11-05 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_officer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officer',
            old_name='admin_id',
            new_name='admin',
        ),
    ]