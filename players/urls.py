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
    path('login/', views.login_page, name = 'l'),
    path('logout/', views.logout_request, name = 'loggedout'),
    path('profile/', views.profile, name = 'profile'),
    path('dashboard/', views.author_dashboard, name = 'dash'),
    path('add_challenges/', views.challenge_form, name = 'add'),
    path('edit_challenges/<int:c_id>/', views.challenge_edit, name = 'edit'),
    path('delete_challenges/<int:c_id>/', views.challenge_delete, name = 'delete'),
    path('send_notification/', views.sending_notification, name='notification'),
    path('notifications/', views.view_notification, name='v_notification'),
    path('test/', views.test, name='testing')
]
