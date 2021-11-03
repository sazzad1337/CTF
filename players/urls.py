from django.contrib import admin
from django.urls import path
from . import views
app_name = "players"
urlpatterns = [
    path('', views.home, name = 'home'),
    path('users/', views.users_list, name = 'users'),
    path('scoreboard/', views.scoreboard, name = 'scoreboard'),
    path('registration/', views.register, name = 'registration'),
    path('challenges/', views.challenges, name = 'challenges'),
    path('f/', views.f, name = ''),
]
