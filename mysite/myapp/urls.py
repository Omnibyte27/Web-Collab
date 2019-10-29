from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #Index page
    path('<int:page>/', views.index),
    #What page you're on
    path('', views.index),
    #View inputs
    path('inputs/', views.inputs_view),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
]
