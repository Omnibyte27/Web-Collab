from django.db import models
from django.contrib.auth.models import User
from django.forms import DecimalField

# Create your models here.

#For chat
class Input(models.Model):
    input = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Renders infomation from object
    def __str__(self):
        return self.author.username + " " + self.input

#For storing card details
class CardCatalogue(models.Model):
    card_id = models.CharField(max_length=5, primary_key=True)
    card_name = models.CharField(max_length=30)
    top_value = models.IntegerField(default = 0)
    left_value = models.IntegerField(default = 0)
    right_value = models.IntegerField(default = 0)
    bottom_value = models.IntegerField(default = 0)
    times_card_played = models.IntegerField(default = 0)

    #Renders infomation from object
    def __str__(self):
        return self.card_id

#User Table
class Players(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=10)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Profile(models.Model):
    p_username = models.OneToOneField(Players, on_delete = models.CASCADE, primary_key=True)
    matches_total = models.IntegerField(default = 0)
    matches_won = models.IntegerField(default = 0)
    matches_lost = models.IntegerField(default = 0)
    success_percentage = DecimalField()
    #rank maybe?
    #rank = models.IntegerField()
    #favorite card?
    #favorite_card = CharField(max_length=10)
    #favorite deck?
    #favorite_deck = CharField(max_length=10)

    def __str__(self):
        return self.p_username.username

class Decks(models.Model):
    cardCatalogue = models.OneToOneField(CardCatalogue, on_delete = models.CASCADE)
    deck_id = models.CharField(max_length=5, primary_key=True)
    deck_name = models.CharField(max_length=10)
    times_deck_played = models.IntegerField(default = 0)
    user = models.ForeignKey(Players, on_delete=models.CASCADE)

    def __str__(self):
        return self.desk_id

class Deck_Contents(models.Model):
    de_desk_id = models.OneToOneField(Decks, on_delete = models.CASCADE, related_name = "desk_id2")
    de_card_id = models.OneToOneField(CardCatalogue, on_delete = models.CASCADE, related_name = "card_id2")

    def __str__(self):
        return self.de_deck_id.deck_id

class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " " + self.comment
