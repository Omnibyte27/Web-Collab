from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm

from django.urls import reverse

# Create your models here.

#For storing card details
class CardCatalogue(models.Model):
    card_id = models.CharField(max_length=5, primary_key=True)
    card_name = models.CharField(max_length=30, unique=True)
    top_value = models.IntegerField()
    left_value = models.IntegerField()
    right_value = models.IntegerField()
    bottom_value = models.IntegerField()

    #Renders infomation from object
    def __str__(self):
        return self.card_name

#For storing profile details
class Profile(models.Model):
    p_username = models.OneToOneField(
        User,
        on_delete = models.CASCADE, 
        primary_key=True        
    )
    matches_won = models.IntegerField(default = 0)
    matches_lost = models.IntegerField(default = 0)
    matches_total = models.IntegerField(default = 0)

    #Renders infomation from object
    def __str__(self):
        return self.p_username.username

#For storing deck details
class Deck(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deck_name = models.CharField(max_length=25, primary_key=True)
    card1 = models.ForeignKey(
        CardCatalogue,
        related_name='card1create',
        on_delete=models.CASCADE,
    )
    card2 = models.ForeignKey(
        CardCatalogue,
        related_name='card2create',
        on_delete=models.CASCADE,
    )
    card3 = models.ForeignKey(
        CardCatalogue,
        related_name='card3create',
        on_delete=models.CASCADE,
    )
    card4 = models.ForeignKey(
        CardCatalogue,
        related_name='card4create',
        on_delete=models.CASCADE,
    )
    card5 = models.ForeignKey(
        CardCatalogue,
        related_name='card5create',
        on_delete=models.CASCADE,
    )     

    #Renders infomation from object
    def __str__(self):
        return self.deck_name

    #Return to deck-page
    def get_absolute_url(self):
        return reverse('deck-page')

#Delete
class UpdateDeck(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deck_name = models.ForeignKey(Deck, on_delete=models.CASCADE)

    #Renders infomation from object
    def __str__(self):
        return self.deck_name
##################################################################
### Keep in
#For chat
class Input(models.Model):
    input = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Renders infomation from object
    def __str__(self):
        return self.author.username + " " + self.input
        
class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " " + self.comment
