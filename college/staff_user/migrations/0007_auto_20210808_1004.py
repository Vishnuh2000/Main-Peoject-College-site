# Generated by Django 3.2.5 on 2021-08-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_user', '0006_auto_20210808_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='sem',
        ),
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=1, verbose_name='semester'),
            preserve_default=False,
        ),
    ]
