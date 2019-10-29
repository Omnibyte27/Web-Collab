from django import forms
from django.core.validators import validate_slug

class InputForm(forms.Form):
    input = forms.CharField(label='Enter text here', max_length=300, validators=[validate_slug])
