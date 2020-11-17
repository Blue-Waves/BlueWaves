from django.forms import ModelForm
from .models import Listing
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ListingForm(ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'category', 'address', 'city', 'description',
                  'price', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'border w-100 p-2 bg-white text-capitalize'}),
            'category': forms.TextInput(attrs={'class': 'border w-100 p-2 bg-white text-capitalize'}),
            'address': forms.TextInput(attrs={'class': 'border w-100 p-2 bg-white text-capitalize '}),
            'city': forms.TextInput(attrs={'class': 'border w-100 p-2 bg-white text-capitalize'}),
            'description': forms.Textarea(attrs={'class': 'border w-100 p-2 bg-white text-capitalize'}),
            'price': forms.TextInput(attrs={'class': 'border w-100 p-2 bg-white text-capitalize'}),
            'photo_main': forms.FileInput(attrs={'class': 'form-control-file'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-lg-6'),
                Column('category', css_class='form-group col-lg-6'),
                css_class='form-row'
            ),

            Row(
                Column('address', css_class='form-group col-lg-6'),
                Column('price', css_class='form-group col-lg-4'),

                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-lg-6'),
                Column('photo_main', 'photo_1', 'photo_2',
                       css_class='form-group col-lg-3'),
                Column('photo_3', 'photo_4', 'photo_5',
                       css_class='form-group col-lg-3'),




                css_class='form-row'
            ),

            Row(
                Column('description', css_class='form-group col-lg-6'),





                css_class='form-row'
            )
        )


class UpdateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'photo_main']
