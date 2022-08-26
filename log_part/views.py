from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))
    return render(request, "admin_part/add_users.html", context={'form': form})


def login_sys(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'log_part/login.html', context=diction)


def logout_sys(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
