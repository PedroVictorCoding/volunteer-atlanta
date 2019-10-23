from django import forms
from .models import Message

class MessageForm(forms.ModelForm):

    
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))

    class Meta:
        model = Message
        fields = (
            'message',
        )
