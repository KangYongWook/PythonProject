from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save() # 회원가입
                auth_login(request, user) # 로그인
                return redirect('window:menu')    
        return render(request, 'signup.html')
    return redirect('window:menu')
        
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('window:menu')
        else:
            return render(request, 'login.html')
    else:
        if request.user.is_authenticated:
            return redirect('window:menu')
        else:
            return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('window:menu')

