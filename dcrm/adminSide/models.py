from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class branch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)
    branch_IP = models.CharField(max_length=50)

    def __str__(self):
        return self.branch_name

class EmployeeManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    POSITION_CHOICES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    branch = models.ForeignKey('branch', on_delete=models.CASCADE, default=1)
    assigned_shift = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

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
    shift_day = models.CharField(max_length=50, choices=DAYS_OF_WEEK)
    shift_branch = models.ForeignKey(branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shift on {self.shift_day} from {self.shift_start} to {self.shift_end} at {self.shift_branch}"

