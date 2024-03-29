from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SignupForm(UserCreationForm):
    username    = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email       = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name   = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))
    password1   = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter Password'}))
    password2   = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password',  'placeholder': 'Re-enter Password'}))


    class Meta:
        model   = User
        fields  = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model   = User
        fields  = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
