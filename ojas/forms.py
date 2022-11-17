from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

# write here class

class SingUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
class contact(forms.Form):
    emp_name=forms.CharField()
    emp_id=forms.IntegerField()
    emp_email=forms.EmailField()
    emp_feedback=forms.CharField()

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'