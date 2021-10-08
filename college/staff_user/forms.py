from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {

            'name': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'semester': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )

        }




class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['department', 'sub', 'semester', 'uploadfile']
        widgets = {

            'department': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sub': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'semester': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'uploadfile': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )


        }
