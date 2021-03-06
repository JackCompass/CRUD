from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from enroll.middleware import RegisterOnLocalHostMiddleware
from .forms import UserRegistration, Registration
from .models import RegisteredAccount
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/accounts/login')
def index(request):
	"""
	Homepage of our CRUD Application.
	It Require the user to be logged in to see this page.
	It render the list of all the the reigstered accounts and also shows a form to add more accounts.
	It also manages the POST request data save it in the database.
	It also validates the form and store the cleaned data into the RegisteredAccount relation.
	"""
	if request.method == "POST":
		form = UserRegistration(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			form = RegisteredAccount(account = request.user, name = name, username = username, email = email, password = password)
			form.save()
			form = UserRegistration()
			return HttpResponseRedirect(reverse('index'))	
	form = UserRegistration()
	accnt = RegisteredAccount.objects.filter(account = request.user)
	ip = request.META.get('REMOTE_ADDR')
	return render(request, 'enroll/user.html', {
		'form' : form,
		'accnt' : accnt,
		'ip' : ip
	})


@login_required(login_url = '/accounts/login')
def remove_account(request, id):
	"""
	It helps to remove the accounts stored by the User.
	For this it makes sure the user is logged in.
	"""
	user = RegisteredAccount.objects.get(pk = id)
	user.delete()
	return HttpResponseRedirect(reverse("index"))


@login_required(login_url = '/accounts/login')
def Updateuser(request, id):
	"""
	This function is called upon when the user want to update a particular registered account details.
	It provides the user with the form filled with all the pre loaded details.
	It manages the POST request data with updating the previous record with the new information.
	It also render all the registered account which is associated with the User account.
	"""
	user = RegisteredAccount.objects.get(pk = id)
	if request.method == 'POST':
		form = UserRegistration(request.POST, instance = user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("index"))

	form = UserRegistration(instance = user)
	accnt = RegisteredAccount.objects.filter(account = request.user)
	return render(request, 'enroll/update.html', {
		'form' : form,
		'accnt' : accnt,
		'id' : id,
	})

@RegisterOnLocalHostMiddleware
def register(request):
	"""
	It directs the user to register into the application without any hassle.
	Handles the POST request data and save the User into the application database.
	"""
	if request.method == 'POST':
		form = Registration(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("login"))
		else:
			return render(request, 'enroll/register.html', {
				'form' : form,
			})
	form = Registration()
	return render(request, 'enroll/register.html', {
		'form' : form,
	})