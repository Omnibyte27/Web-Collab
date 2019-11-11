from django.db import models
from django.contrib.auth.models import User

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
    top_value = models.IntegerField()
    left_value = models.IntegerField()
    right_value = models.IntegerField()
    bottom_value = models.IntegerField()
    times_card_played = models.IntegerField(default=0)

    #Renders infomation from object
    def __str__(self):
        return self.card_id
        
class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " " + self.comment