# Generated by Django 4.0.1 on 2022-01-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0008_remove_mathtutor_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
