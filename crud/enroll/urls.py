from django.urls import path
from enroll import views

"""Defining app name to reference the url later."""
app_name = 'crud'


urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('', v.index, name = 'index'),
	path('remove/<int:id>', v.remove_account, name="delete"),
	path('update/<int:id>', v.Updateuser, name="update"),
	path('register/', v.register, name="register"),
	]