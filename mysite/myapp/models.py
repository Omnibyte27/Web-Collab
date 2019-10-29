from django.db import models

# Create your models here.
class Input(models.Model):
    input = models.CharField(max_length=300)
    
    #Renders infomation from object
    def __str__(self):
        return self.input
