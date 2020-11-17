from django import forms
from Core.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'phone',
            'email',
            
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),

        }

        
        # exclude = {} can be used to miminze number of lines coz you just pass in what you want to exclude
