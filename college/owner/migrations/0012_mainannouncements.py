# Generated by Django 3.2.5 on 2021-08-01 04:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0011_alter_teachers_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAnnouncements',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='announcement/file', verbose_name='upload file')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
