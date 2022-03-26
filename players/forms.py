from django import forms
from players import models
from .models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChallengsForm(forms.ModelForm):
    class Meta:
        model = models.Challenges
        fields = ('c_name', 'c_category', 'c_description', 'c_point','c_flag',)
        labels  = {
        'c_name':'Challenge Name', 
        'c_category':'Category', 
        'c_description':'Description', 
        'c_point':'Points', 
        'c_flag':'Flag'
        }
        widgets = {
        'c_name': forms.TextInput(attrs={'class':'form-control'}),
        'c_category': forms.TextInput(attrs={'class':'form-control'}),
        'c_description': forms.Textarea(attrs={'class':'form-control'}),
        'c_point': forms.NumberInput(attrs={'class':'form-control'}),
        'c_flag': forms.TextInput(attrs={'class':'form-control'}),
        } 

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


class NotifyForm(forms.ModelForm):
    class Meta:
        model = models.Notify
        fields = ['info']
        labels  = {
        'info':'Enter Details'
        }
        widgets = {
        'info': forms.TextInput(attrs={'class':'form-control'})
        } 

class RulesForm(forms.ModelForm):
    class Meta:
        model = models.Rules
        fields = ['details']
        labels  = {
        'details':'Enter Details'
        }
        widgets = {
        'details': forms.Textarea(attrs={'class':'form-control'})
        } 