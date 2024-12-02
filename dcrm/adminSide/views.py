from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #log in check
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return render(request, 'home.html', {})
        else:
            messages.success(request, "There was an error logging in. Please try again.")
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
    
def shiftC(request):
    return render(request, 'shift.html', {})

def notifications(request):
    return render(request, 'notifs.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')