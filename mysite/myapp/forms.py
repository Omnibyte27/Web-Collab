from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelChoiceField
from django.forms import ModelForm
from myapp.models import Deck
from myapp.models import CardCatalogue
from myapp.models import Challenge

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ["deck_name", "card1", "card2", "card3", "card4", "card5"]

class VersusDeck(ModelForm):
    class Meta:
        model = Challenge
        fields = ["user_from_deck", "user_to_deck"]

class InputForm(forms.Form):
    input = forms.CharField(label='Enter message here', max_length=100, validators=[validate_slug])
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
