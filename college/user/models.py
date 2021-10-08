from django.db import models
from accounts.models import *





class ContactUs(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Name'
    )
    subject = models.CharField(
        max_length=100,
        verbose_name='Subject'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    message = models.TextField(
        verbose_name='Message'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
