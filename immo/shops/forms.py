from django import forms

class HomeForm(forms.Form):
    location = forms.CharField()
