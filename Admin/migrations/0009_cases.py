# Generated by Django 3.0.4 on 2020-11-10 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_auto_20201106_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('case_id', models.IntegerField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=50)),
                ('case_type', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('type_of_weapon', models.CharField(blank=True, max_length=255)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('officer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin', to='Admin.Admin')),
            ],
        ),
    ]
