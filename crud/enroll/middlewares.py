from django.http import HttpResponse
from django.urls import reverse_lazy

class RegisterOnLocalHostMiddleware:
	"""
	Creating a middleware which bound the registration page access only to the localhost Users.
	Other users will get a 500 status code.
	Http status code 500 : The HyperText Transfer Protocol (HTTP) 500 Internal Server Error server error
	response code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.
	Middleware can be disabled by removing this specific middleware from settings.py file.

	"""
	def __init__(self, get_response):
		self.get_response = get_response
		self.blocked_path = reverse_lazy(viewname = 'register')
		self.localhost = '127.0.0.1'
		
	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, *args, **kwargs):
		"""This method handles the incoming data with the request too"""
		if request.path == self.blocked_path and request.META.get('REMOTE_ADDR') != self.localhost:
			return HttpResponse(status = 500)
		return None