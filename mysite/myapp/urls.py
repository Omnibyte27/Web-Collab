from django.urls import path, include


from . import views

urlpatterns = [
    #Index page
    path('<int:page>/', views.index),
    #What page you're on
    #path('', views.index),
    #View inputs
    path('inputs/', views.inputs_view),
    #Project urls
    
    path('', views.main_page),
    #path('main_page/', views.main_page),
    path('profile/', views.profile),
    path('decks/', views.decks),
    path('play/', views.play),
]
