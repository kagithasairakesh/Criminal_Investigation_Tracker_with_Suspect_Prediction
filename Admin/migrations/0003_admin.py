# Generated by Django 3.0.4 on 2020-11-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/admin/')),
                ('phone_number', models.CharField(max_length=12)),
                ('mail_id', models.EmailField(max_length=50)),
            ],
        ),
    ]
