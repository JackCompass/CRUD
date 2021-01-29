from django.http import HttpResponse

def RegisterOnLocalHostMiddleware(get_response):
	"""
	Creating a middleware which bound the registration page access only to the localhost Users.
	Other users will get a 500 status code.
	Http status code 500 : The HyperText Transfer Protocol (HTTP) 500 Internal Server Error server error
	response code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.
	Middleware can be disabled by removing this specific middleware from settings.py file.

	"""
	localhost = '127.0.0.1'
	def middleware(request):
		if request.META.get('REMOTE_ADDR') != localhost:
			return HttpResponse(status = 500)
		else:
			response = get_response(request)
		return response
	return middleware