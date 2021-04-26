from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from django.core import validators


class UserForm(UserCreationForm):
    '''form for creating a user'''


    terms = forms.BooleanField(
    error_messages={'required': 'You must accept terms and conditions'},
    )

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','email','first_name',
                  'last_name','password1','password2')


class TypesForm(forms.Form):

    commonusers = forms.BooleanField(required=False)

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


