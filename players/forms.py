from django import forms
from players import models
from .models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChallengsForm(forms.ModelForm):
    class Meta:
        model = models.Challenges
        fields = "__all__"

class PlayerRegister(forms.ModelForm):
    class Meta:
        model = models.players_list
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country']