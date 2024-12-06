from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import branch, Shift, Employee
from .forms import BranchForm, EmployeeForm

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
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = EmployeeForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def view_branch(request, pk):
    branch_info = branch.objects.get(branch_id=pk)  # Ensure this retrieves the correct branch
    shifts = Shift.objects.filter(shift_branch=branch_info)
    employees_by_shift = {}

    for shift in shifts:
        employees_by_shift[shift.shift_id] = Employee.objects.filter(assigned_shift=shift.shift_id)

    employees = Employee.objects.all()

    return render(request, 'branch.html', {
        'branch_info': branch_info,  # Ensure this contains branch_id
        'shifts': shifts,
        'employees_by_shift': employees_by_shift,
        'employees': employees,
    })



def add_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Branch added successfully!")
            return redirect('home')
        else:
            # Log or print the errors for debugging
            print(form.errors)
            messages.error(request, "Failed to add branch. Check the form for errors.")
            return render(request, 'add_branch.html', {'form': form})
    else:
        form = BranchForm()
    return render(request, 'add_branch.html', {'form': form})

def assign_employee_to_shift(request):
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        employee_id = request.POST.get('employee_id')
        branch_id = request.POST.get('branch_id')  # Ensure the branch_id is retrieved

        # Debugging logs
        print(f"shift_id: {shift_id}")
        print(f"employee_id: {employee_id}")
        print(f"branch_id: {branch_id}")  # Check if this prints correctly

        # Ensure the branch_id is not empty
        if not branch_id:
            messages.error(request, "Invalid branch.")
            return redirect('home')  # Redirect to a default view or error page

        # Validate employee_id is not empty and is a number
        if not employee_id or not employee_id.isdigit():
            messages.error(request, "Please select a valid employee.")
            return redirect('branch', pk=branch_id)  # Use the branch_id here

        shift = Shift.objects.get(shift_id=shift_id)

        # Ensure employee_id is an integer
        employee = Employee.objects.get(employee_id=int(employee_id))

        # Assign the employee to the shift using shift_id
        employee.assigned_shift = shift.shift_id  # Assign the shift_id instead of the Shift object
        employee.save()

        messages.success(request, f"{employee.first_name} {employee.last_name} has been assigned to the shift.")

        # Redirect back to the correct branch page with the correct branch_id
        return redirect('branch', pk=branch_id)  # Ensure the branch_id is passed in the redirect
    else:
        messages.error(request, "Invalid request method.")
        return redirect('home')  # Redirect to a default view or error page






