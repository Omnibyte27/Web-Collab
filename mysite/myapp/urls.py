from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    DeckDetailView,
    DeckUpdateView,
    DeckDeleteView
)

urlpatterns = [
    #Project urls
    path('', views.index, name='main-page'),
    path('profile/', views.profile, name='profile-page'),
    path('play/', views.play, name='play-page'),  
    path('inputs/', views.inputs_view),
    #Deck urls
    path('decks/', views.decks, name='deck-page'),
    path('deck/<str:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('deck/<str:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('deck/<str:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    #Login/Logout/Register urls
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
]
