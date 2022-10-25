from django import forms

class Forms(forms.Form):
    content = forms.Textarea()