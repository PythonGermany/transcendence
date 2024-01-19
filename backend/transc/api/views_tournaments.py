from django.utils.decorators import method_decorator
from .decorators import *
from django.views import View
from django.http import JsonResponse
from .models import Tournament
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime

# Endpoint: /tournaments
@method_decorator(login_required, name='dispatch')
class TournamentCollection(View):
	@method_decorator(staff_required, name='dispatch')
	def get(self, request):
		tournaments = Tournament.objects.all()
		data = {
			'tournaments': [t.serialize() for t in tournaments],
			'count': tournaments.count(),
		}
		return JsonResponse(data)

	@check_body_syntax(["title", "description"])
	def post(self, request):
		tournament_data = {
				'title': self.body.get('title'),
				'description': self.body.get('description'),
				'creator': request.user.id,
				#'status': TournamentStatus::CREATED - set at DB level
			}
		t = Tournament.objects.create(**tournament_data)
		return JsonResponse(t.serialize(), status=201, safe=False)

# Endpoint: /tournaments/<int:tournament_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Tournament, 'tournament_id', 
																			'Tournament does not exist'), name='dispatch')
class TournamentSingle(View):
	def get(self, request, tournament_id):
		t = Tournament.objects.get(pk=tournament_id)
		return JsonResponse({'tournament': t.serialize()})

	# allow only update of title and description
	@check_body_syntax(["title", "description"])
	def patch(self, request, tournament_id):
		t = Tournament.objects.get(pk=tournament_id)
		t.title = self.body.get('title')
		t.description = self.body.get('description')
		t.updated_at = datetime.datetime.now()
		t.save()
		return JsonResponse(t.serialize(), status=200, safe=False)

	@staff_required
	def delete(self, request, tournament_id):
		Tournament.objects.get(pk=tournament_id).delete()
		return JsonResponse({}, status=204)
