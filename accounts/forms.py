from django import forms
from Core.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'phone',
            'email',
            'first_name',
            'last_name',
            'password'
        }
        # exclude = {} can be used to miminze number of lines coz you just pass in what you want to exclude
