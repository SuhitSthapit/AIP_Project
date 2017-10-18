from django import forms

class SubmitGithubUser(forms.Form):
    name = forms.CharField()