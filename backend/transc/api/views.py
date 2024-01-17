from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .decorators import login_required, check_body_syntax
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

def index(request):
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

class Login(View):
	@check_body_syntax(['name', 'password'])
	def post(self, request):
		user = authenticate(username=self.body.get('name'), 
												password=self.body.get('password'))
		if user is None:
			return JsonResponse({"reason": "Invalid login credentials"}, status=401)
		login(request, user)
		return JsonResponse({'message': 'Login successful'})