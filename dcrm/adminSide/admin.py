from django.contrib import admin
from .models import branch
from .models import Employee
from .models import Shift

# Register your models here.
admin.site.register(branch)
admin.site.register(Employee)
admin.site.register(Shift)