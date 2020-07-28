from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from counter.forms import SignUpForm, LoginForm
from django.contrib import messages


def index(request):
    return render(request, 'counter/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f"{form.cleaned_data['username']} is already in use")
                return redirect(reverse('counter:signup'))
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'{user.username} successfully created !')
            user_logged = authenticate(request, **form.cleaned_data)
            login(request, user_logged)
            return redirect(reverse('counter:homepage'))
    else:
        form = SignUpForm()

    return render(request, 'counter/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, 'Successfully logged in!')
                return redirect(reverse('counter:homepage'))
            else:
                messages.error(request, 'Bad authentication....')
                return redirect(reverse('counter:login'))

    else:
        form = LoginForm()

    return render(request, 'counter/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('counter:index'))


@login_required
def profile(request):
    return render(request, 'counter/profile.html')


def homepage(request):
    return render(request, 'counter/homepage.html')
