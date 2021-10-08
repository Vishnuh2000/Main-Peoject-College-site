from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields=[ 'name' , 'subject' , 'message' ]
        widgets={
            'name' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your name'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Subject'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Message'
                }
            )
            
        }

       
