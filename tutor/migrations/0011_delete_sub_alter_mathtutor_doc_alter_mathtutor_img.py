# Generated by Django 4.0.1 on 2022-01-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0010_alter_sub_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sub',
        ),
        migrations.AlterField(
            model_name='mathtutor',
            name='doc',
            field=models.FileField(default=1, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='mathtutor',
            name='img',
            field=models.ImageField(default=1, upload_to='upload/'),
        ),
    ]