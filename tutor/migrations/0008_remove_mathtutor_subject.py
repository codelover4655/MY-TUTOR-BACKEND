# Generated by Django 4.0.1 on 2022-01-24 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_sub_alter_mathtutor_matutor_mathtutor_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mathtutor',
            name='subject',
        ),
    ]