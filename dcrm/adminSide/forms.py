from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import branch
from .models import Employee

class BranchForm(forms.ModelForm):
    class Meta:
        model = branch
        fields = ['branch_name', 'branch_address', 'branch_IP']

    branch_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    branch_address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    branch_IP = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'email', 'branch']
        widgets = {
            'branch': forms.Select(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
