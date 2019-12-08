from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone

# Create your models here.

#For storing developer messages
class DevMessages(models.Model):
    m_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    post = models.CharField(max_length=500, blank=True)

    #Renders infomation from object
    def __str__(self):
        return self.title

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

#For storing deck details
class Deck(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "d_author")
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

##################################################################
class Challenge(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')
    user_from_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='user_from_deck')
    user_to_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='user_to_deck')
    created_at = models.DateTimeField(auto_now_add=True)

    #Renders infomation from object
    def __str__(self):
        return str(self.user_from.username) + " combined their deck \"" + str(self.user_from_deck) + "\" with " + str(self.user_to.username) + "\'s deck \"" + str(self.user_to_deck) + "\""

##################################################################
###For chat
class Input(models.Model):
    input = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Renders infomation from object
    def __str__(self):
        return self.author.username + " " + self.input
