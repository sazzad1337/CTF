from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
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
    path('test/', views.test, name='testing'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='players/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="players/password/password_reset_confirm.html",success_url="/reset/done/"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='players/password/password_reset_complete.html'), name='password_reset_complete'), 
]
