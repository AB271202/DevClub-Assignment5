from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'success.html', {'username':username})
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Try again")

    return render(request, 'Home.html')


def loginsuccess(request):
    return render(request, 'success.html')
