from django.contrib import admin

from . import models

# Register your models here.

# Admin
admin.site.register(models.Input)
admin.site.register(models.Comment)
# Project
admin.site.register(models.CardCatalogue)
admin.site.register(models.Profile)
admin.site.register(models.Deck)