from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RegisteredAccount(models.Model):
	"""
	Schema of the RegisteredAccount table inside the database. 
	"""
	account = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 50)
	username = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	password = models.CharField(max_length = 50)