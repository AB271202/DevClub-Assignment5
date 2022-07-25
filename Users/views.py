from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'success.html', {'username': username})
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Try again!")

    return render(request, 'Home.html')


def logout_user(request):
    logout(request)
    return redirect('Home')


def register_user(request):
    form = RegistrationForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(user)
            messages.success(request,'Registered successfully!')
            return render(request, 'success.html', {'username': username})
        else:
            form = RegistrationForm(request.POST)

    return render(request, 'reguser.html',{'form':form})
