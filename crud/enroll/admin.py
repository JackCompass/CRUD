from django.contrib import admin
from .models import RegisteredAccount
# Register your models here.

# Registering the RegisteredAccount model and also 
# modifying the view of the data in the admin panel.
@admin.register(RegisteredAccount)
class RegisteredAccountAdmin(admin.ModelAdmin):
	list_display = ('name', 'username')
	exclude = ('account', 'email', 'password')
	readonly_fields = ('username',)
	list_display_links = ('username',)