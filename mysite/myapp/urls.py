from django.urls import path, include, re_path
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
    path('players/', views.players_view),
    path('inputs/', views.inputs_view),
    #Deck Combination
    path('user_from/', views.from_view),
    path('user_to/', views.to_view),
    #Game
    re_path(r'^game/(?P<player>\w+)/$', views.player_view, name='p_view'),
    re_path(r'^game/(?P<player>\w+)/matching/$', views.matching_view, name='g_view'),
    path('decks/', views.decks, name='deck-page'),
    #Deck
    path('deck/<str:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('deck/<str:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('deck/<str:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    #Login/Logout/Register urls
    path('login/', auth_views.LoginView.as_view(), name='login-page'),
    path('logout/', views.logout_view),
    path('register/', views.register),
]
