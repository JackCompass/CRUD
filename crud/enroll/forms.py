from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegisteredAccount


class UserRegistration(forms.ModelForm):
	"""
	Form to add different accounts of a particular user inside the application.
	"""
	class Meta:
		model = RegisteredAccount
		fields = ['name', 'username', 'email', 'password']
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control'}),
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.TextInput(attrs={'class':'form-control'}),
			'password' : forms.TextInput(attrs={'class':'form-control'}),
		}

class Registration(UserCreationForm):
	"""
	A User registration form to register user on the website.
	"""
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')