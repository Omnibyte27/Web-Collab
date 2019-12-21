from django.contrib import admin
from . import models

# Register your models here.

# Admin
admin.site.register(models.DevMessages)
# Chat
admin.site.register(models.Input)
#Game
admin.site.register(models.Deck)
admin.site.register(models.CardCatalogue)
admin.site.register(models.Challenge)