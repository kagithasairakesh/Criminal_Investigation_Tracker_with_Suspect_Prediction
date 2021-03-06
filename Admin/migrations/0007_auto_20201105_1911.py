# Generated by Django 3.0.4 on 2020-11-05 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Admin', '0006_auto_20201105_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin_officers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='officer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_officer', to=settings.AUTH_USER_MODEL),
        ),
    ]
