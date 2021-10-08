from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, EmailValidator
from django.core import validators


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'type' :'email'
                }

            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }

            ),
        }








class StaffRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'type' :'email'
                }

            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
    

            ),
        }




class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }

            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'type' :'email'
                }

            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
    

            ),
        }

