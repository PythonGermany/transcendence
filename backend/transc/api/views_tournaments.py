from django.utils.decorators import method_decorator
from .decorators import *
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Tournament
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime

# Endpoint: /tournaments
@method_decorator(check_structure("/tournaments"), name='dispatch')
class TournamentCollection(View):
	def get(self, request):
		tournaments = Tournament.objects.all()
		return JsonResponse([t.serialize() for t in tournaments], safe=False)

	def post(self, request):
		tournament = Tournament.objects.create(
			title=request.json.get('title'),
			description=request.json.get('description', ''),
			creator=request.user
		)

		tournament.players.add(request.user)

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize(), status=201)

# Endpoint: /tournaments/TOURNAMENT_ID
@method_decorator(check_structure("/tournaments/TOURNAMENT_ID"), name='dispatch')
@method_decorator(check_object_exists(Tournament, 'tournament_id', 
																			TOURNAMENT_404), name='dispatch')
class TournamentSingle(View):
	def get(self, request, tournament_id):
		t = Tournament.objects.get(id=tournament_id)
		return JsonResponse(t.serialize())

	def patch(self, request, tournament_id):
		tournament = Tournament.objects.get(id=tournament_id)
		if request.json.get('title') is not None:
			tournament.title = request.json.get('title')
		if request.json.get('description') is not None:
			tournament.description = request.json.get('description')
		player_username = request.json.get('player')
		if player_username is not None:
			player = User.objects.get(username=player_username)
			tournament.players.add(player)
		tournament.save()

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize())

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, tournament_id):
		Tournament.objects.get(id=tournament_id).delete()

		# TODO: Implement websocket notification?

		return HttpResponse(status=204)
