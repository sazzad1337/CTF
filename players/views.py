from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from players import forms

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .models import Profile
from .models import Challenges

import datetime

# Create your views here.
from .models import * #or users_list

def users_list(request):
    user = User.objects.values()
    co = Profile.objects.values()
    diction = {'players_list': user, 'title': "Users", 'con':co}
    return render(request, 'players/users.html', context = diction)


def home(request):
    diction = {'title': "Home"}
    return render(request, 'players/home.html', context = diction)


def test(request):
    if request.method == 'POST':
        d = request.POST.get('sub_flag')
        print(d)
        c = request.POST.get('ori_flag')
        print(c)
        if d == c:
            print('congo')
    cl = Challenges.objects.order_by('c_flag')

    diction = {'title': "Challenges", 'c': 's'}
    return render(request, 'players/test.html', context = diction)



@login_required
def challenges(request):
    challenges_list = Challenges.objects.values()
    if request.method == 'POST':
        d = request.POST.get('submitted_flag')
        challenge_id = request.POST.get('x')
        p = request.POST.get('p')
        checking = Challenges.objects.filter(id=challenge_id)
        print(checking)
        for x in checking:
            print(x.c_flag)
            if x.c_flag == d:
                current_user = User.objects.get(id=request.user.id)
                double_check = score.objects.filter(solved=challenge_id,solver_name_id=current_user).exists()
                if double_check == True:
                    messages.warning(request,"You have already solved this challenge.")
                else:
                    messages.success(request,"Congratulations! Your answer is correct.")
                    current_cpoint = x.c_point
                
                    current_time = datetime.datetime.now()
                    s = score(solver_name=current_user, time=current_time, solved_id=challenge_id, points=current_cpoint)
                    s.save()
                    print(current_time)
            else:
                messages.error(request,"Your Answer is incorrect!")


    diction = {'title': "Challenges", 'challenges_list': challenges_list}
    return render(request, 'players/challenges.html', context = diction)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if request.user.is_staff:
                    return redirect("players:dash")
                else:
                    return redirect("players:challenges")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    diction = {'title': "Login", 'form':form}
    return render(request, 'players/login.html', context = diction)


def logout_request(request):
    diction = {'title':"Logged Out"}
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return render(request, 'players/logout.html', context = diction)




def scoreboard(request):
    p = score.objects.raw('SELECT solver_name_id, time, id, Sum(points) AS total FROM players_score GROUP BY solver_name_id ORDER BY total DESC')
    print(p)
    diction = {'title':"Scoreboard",'scores':p}
    return render(request, 'players/scoreboard.html', context = diction)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account is created successfully')
            return redirect('players:l')
    else:
        form = UserRegisterForm()

    diction = {'title': "Registration", 'form':form}
    return render(request, 'players/register.html', context = diction)


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('players:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    diction = {'title':"Profile", 'u_form':u_form, 'p_form':p_form}
    return render(request, 'players/profile.html', context = diction)



def challenge_form(request):
    form = forms.ChallengsForm()
    if request.method == "POST":
        form = forms.ChallengsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return author_dashboard(request)
    diction = {'title': "Challenges", "challenges":form}
    return render(request, 'author/challenge_form.html', context = diction)

def author_dashboard(request):
    c_list = Challenges.objects.values()
    diction = {'title': "Dashboard", 'list':c_list}
    return render(request, 'author/home.html', context = diction)


def challenge_edit(request,c_id):
    c_info = Challenges.objects.get(pk=c_id)
    form = forms.ChallengsForm(instance=c_info)

    if request.method =="POST":
        form = forms.ChallengsForm(request.POST, instance=c_info)

        if form.is_valid():
            form.save(commit=True)
            return author_dashboard(request)
    diction = {'title':"Edit Challenges", 'c_info':form}
    return render(request, 'author/challenge_info.html', context = diction)


def challenge_delete(request,c_id):
    c_info = Challenges.objects.get(pk=c_id).delete()
    diction = {'delete_message': "Deleted Sucessfully"}
    return render (request, 'author/challenge_delete.html', context = diction)

def sending_notification(request):
    form = forms.NotifyForm()
    if request.method == "POST":
        form = forms.NotifyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return author_dashboard(request)
    diction = {'title': "Notification", 'noti':form}
    return render (request, 'author/notifications.html', context = diction)

def view_notification(request):
    n = Notify.objects.values()
    diction = {'title': "Challenges", 'n': n}
    
    return render(request, 'players/notification.html', context = diction)