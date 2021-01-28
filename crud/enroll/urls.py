from django.urls import path
from enroll import views

"""Defining app name to reference the url later."""
app_name = 'crud'


urlpatterns = [
		path('', views.home, name = "home"),
	]