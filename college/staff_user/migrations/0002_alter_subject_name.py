# Generated by Django 3.2.5 on 2021-08-04 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0012_mainannouncements'),
        ('staff_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.department', verbose_name='Department'),
        ),
    ]
