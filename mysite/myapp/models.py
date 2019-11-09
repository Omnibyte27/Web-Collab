from django.db import models

# Create your models here.
class Input(models.Model):
    input = models.CharField(max_length=300)
    
    #Renders infomation from object
    def __str__(self):
        return self.input


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