from django.shortcuts import render
from django.http import HttpResponse
from players import forms

# Create your views here.
from .models import * #or users_list
def users_list(request):
    user = players_list.objects.order_by('username')
    diction = {'players_list': user, 'title': "Users"}
    return render(request, 'players/users.html', context = diction)


def home(request):
    diction = {'title': "Home"}
    return render(request, 'players/home.html', context = diction)

def challenges(request):
    diction = {'title': "Challenges"}
    return render(request, 'players/challenges.html', context = diction)

def f(request):
    diction = {'title': "Challenges"}
    return render(request, 'players/footer.html', context = diction)
    
def scoreboard(request):
    diction = {'title':"Scoreboard"}
    return render(request, 'players/scoreboard.html', context = diction)

def register(request):
    form = forms.PlayerRegister()
    if request.method == "POST":
        form = forms.PlayerRegister(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
    diction = {'title': "Registration", "reg_form":form}
    return render(request, 'players/register.html', context = diction)