from django import forms

class WordForm(forms.Form):
    user_input =  forms.CharField(widget=forms.Textarea)