from django.db import models

# Create your models here.
class branch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)
    branch_IP = models.CharField(max_length=50)
    branch_Shifts = models.CharField(max_length=50)
    branch_emps = models.CharField(max_length=50)

    def __str__(self):
        return self.branch_name

class Employee(models.Model):
    POSITION_CHOICES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='Employee')
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)  # Link to the Branch model
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shift(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    shift_id = models.AutoField(primary_key=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    shift_day = models.CharField(max_length=50, choices=DAYS_OF_WEEK)  # Dropdown for weekdays
    shift_branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, related_name='shifts')  # Many-to-many relationship

    def __str__(self):
        return f"Shift on {self.shift_day} from {self.shift_start} to {self.shift_end} at {self.shift_branch}"

