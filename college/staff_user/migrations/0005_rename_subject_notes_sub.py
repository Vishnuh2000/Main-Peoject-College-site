# Generated by Django 3.2.5 on 2021-08-08 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_user', '0004_auto_20210808_0844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='subject',
            new_name='sub',
        ),
    ]
