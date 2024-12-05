from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import branch

# Create your views here.



def home(request):
    branches = branch.objects.all()  # Fetch all branch objects
    return render(request, 'home.html', {'branches': branches})  # Pass them as 'branches'


def login_user(request):
    #log in check
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Please try again.")
            return render(request, 'login.html', {})
    
    return render(request, 'login.html', {})
    
def shiftC(request):
    return render(request, 'shift.html', {})

def notifications(request):
    return render(request, 'notifs.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def view_branch(request, pk):
    branch_info = branch.objects.get(branch_id=pk)
    return render(request, 'branch.html', {'branch_info': branch_info})
