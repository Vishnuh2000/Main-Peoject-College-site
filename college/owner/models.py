from django.db import models
from ckeditor.fields import RichTextField


class Department(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    Name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Name',
    )
    Description = RichTextField(
        verbose_name='Description'
    )
    image = models.ImageField(
        upload_to='uploads',
        verbose_name='Department Image'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.Name


class Activity(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Name'
    )
    Description = RichTextField(
        verbose_name='Description'
    )
    activity_image = models.ImageField(
        blank=True,
        upload_to='Activity_uploads',
        verbose_name='Activity images'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )



class Facilities(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Facility name'
    )
    Description = RichTextField(
        verbose_name='Description'
    )
    image = models.ImageField(
        verbose_name='Facility image'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )


class Teachers(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Teachers Name',
        null=True,
        blank=True,
    )
    Name = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        verbose_name='Department Name'
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Position'
    )
    Email = models.EmailField(
        unique=True,
        verbose_name='Email Address',
        null=True,
        blank=True,
    )
    Phone = models.IntegerField(
        verbose_name='Phone Number',
         null=True,
         blank=True,
    )
    T_image = models.ImageField(
        upload_to = 'Teachers_photo',
        verbose_name='Image',
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )




class MainAnnouncements(models.Model):
    id= models.BigAutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Title'
    )
    description = RichTextField(
        verbose_name='Description'
    )
    pdf = models.FileField(
        upload_to='announcement/file',
        verbose_name='upload file',
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )