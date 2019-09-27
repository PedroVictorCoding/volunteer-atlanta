from django import forms

class HomeForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-group'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group'}))
    website = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Enter Website (Recommend: Google Forms)'}))
