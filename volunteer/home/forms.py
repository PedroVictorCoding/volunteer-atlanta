from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):

    title       = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))

    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description + Requirements'}), )

    website     = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Website (Recommended: Google Forms)'}))

    address     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}))



    class Meta:
        model   = Post
        fields  = (
            'title',
            'description',
            'website',
            'address',
            )
