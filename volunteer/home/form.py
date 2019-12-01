from django import forms
from home.models import Post
from home.models import VolunteeringLog, VolunteeringQuestions

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


class LogForm(forms.ModelForm):

    agency_name         = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Agency Name'}))

    activity            = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Volunteering Activity'}), )

    hours               = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hours Earned'}))

    date_activity       = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date(s) of Activity'}))

    supervisor_contact  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Supervisor's Name and Contact"}))

    signature           = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': '', 'style': 'visibility:hidden', 'id': 'signatureArray'}))

    class Meta:
        model   = VolunteeringLog
        fields  = (
            'agency_name',
            'activity',
            'hours',
            'date_activity',
            'supervisor_contact',
            'signature'
            )

class VolunteerQuestionsForm(forms.ModelForm):
    q1 = 'Question1'
    q2 = 'Question2'
    q3 = 'Question3'
    q4 = 'Question4'
    question1 = forms.CharField(required=False, label=q1, widget=forms.Textarea(attrs={'id': 'q1', 'class': 'form-control','rows': '2', 'placeholder': 'Enter your Answer'}))
    question2 = forms.CharField(required=False, label=q2, widget=forms.Textarea(attrs={'id': 'q2', 'class': 'form-control','rows': '2', 'placeholder': 'Enter your Answer'}))
    question3 = forms.CharField(required=False, label=q3, widget=forms.Textarea(attrs={'id': 'q3', 'class': 'form-control','rows': '2', 'placeholder': 'Enter your Answer'}))
    question4 = forms.CharField(required=False, label=q4, widget=forms.Textarea(attrs={'id': 'q4', 'class': 'form-control','rows': '2', 'placeholder': 'Enter your Answer'}))

    class Meta:
        model = VolunteeringQuestions
        fields = (
            'question1',
            'question2',
            'question3',
            'question4',
        )
