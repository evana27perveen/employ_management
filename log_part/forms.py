from django.contrib.auth.forms import forms
from .models import DepartmentModel, EmployeeProfileModel, ManagerModel
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        exclude = ('', )


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfileModel
        exclude = ('',)


class ManagerForm(forms.ModelForm):
    class Meta:
        model = ManagerModel
        exclude = ('',)
