from django.contrib import admin

from . import models

# Register your models here.

# Admin
admin.site.register(models.Input)
# Project
admin.site.register(models.CardCatalogue)
admin.site.register(models.DevMessages)
admin.site.register(models.Deck)
#Game
admin.site.register(models.Challenge)