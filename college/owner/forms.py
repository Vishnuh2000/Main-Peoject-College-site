from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Department Name'
                }
            ),
            'Description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'activity_image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Name': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'position': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Phone': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'T_image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }



class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model=MainAnnouncements
        fields = '__all__'
        widgets = {

            'title' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'pdf' : forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }