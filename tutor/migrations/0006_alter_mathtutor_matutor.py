# Generated by Django 4.0.1 on 2022-01-23 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0005_mathtutor_lati_mathtutor_longi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathtutor',
            name='matutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
