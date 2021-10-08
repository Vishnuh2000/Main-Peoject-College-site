from django.db import models
from owner.models import *


class Subject(models.Model):
    SEM_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    )

    id = models.BigAutoField(
        primary_key=True
    )
    name = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        verbose_name='Department'
    )
    subject = models.CharField(
        max_length=100,
        verbose_name='Subject'
    )
    semester = models.CharField(
        max_length=100,
        choices=SEM_CHOICE,
        verbose_name='Semester'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return self.subject


class Notes(models.Model):
    SEM_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    )
    id = models.BigAutoField(
        primary_key=True
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        verbose_name='Department'
    )
    sub = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        verbose_name='Subject',
        related_name='sub'
    )
    semester = models.CharField(
        max_length=100,
        choices=SEM_CHOICE,
        verbose_name='semester',
    )
    uploadfile = models.FileField(
        upload_to='Notes',
        verbose_name='Upload File'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
