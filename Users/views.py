from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm, SCompleteRegistrationForm, PCompleteRegistrationForm, ACompleteRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Instructor, Admin


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('success')
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Try again!")

    return render(request, 'Home.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('Home')


def register_user(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Please continue registering')
            return redirect('completereg')
            # Here if I use render then it doesn't go to the url and the complete_reg method is not called
        else:
            form = RegistrationForm(request.POST)

    return render(request, 'reguser.html', {'form': form})


def complete_reg(request):
    username = request.user.username
    if username[0] == 'S':
        form = SCompleteRegistrationForm(request.POST)
    elif username[0] == 'P':
        form = PCompleteRegistrationForm(request.POST)
    else:
        form = ACompleteRegistrationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            if username[0] == 'S':
                form = SCompleteRegistrationForm(request.POST)
            elif username[0] == 'P':
                form = PCompleteRegistrationForm(request.POST)
            else:
                form = ACompleteRegistrationForm(request.POST)

    return render(request, 'completereg.html', {'form': form})


def success(request):
    return render(request, 'success.html', {'user': request.user})
