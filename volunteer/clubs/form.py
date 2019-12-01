from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from clubs.models import CheerItems

class CheerItemsForm(forms.ModelForm):

    items = forms.CharField(
        required=True,
        error_messages={'required': 'Select Items to continue'},
        widget=forms.TextInput( attrs={'style': 'visibility:block', 'readonly': 'readonly', 'id': 'itemsInput'})
        )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter a Note for the Coach. (Not Required)'})
    )

    class Meta:
        model = CheerItems
        fields = (
            'items',
            'notes'
        )
