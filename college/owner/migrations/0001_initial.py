# Generated by Django 3.2.4 on 2021-06-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('Description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='uploads', verbose_name='Department Image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]