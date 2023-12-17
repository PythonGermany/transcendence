from django.views import View
from django.http import JsonResponse, Http404
from .models import User
from .models import Game
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .serials import serialize_game
import json
import datetime

# GET/POST  /games
class GameView(View):
	def post(self, request):
		data = json.loads(request.body.decode("utf-8"))
		game_id = data.get('game_id')
		player_id = data.get('player_id')
		player2_id = data.get('player2_id')

		game_data = {
			'game_id': game_id,
			'player_id': player_id,
			'player2_id': player2_id,
			#'status': GameStatus::CREATED - set at DB level
			#'created_at': datetime.datetime.now()
		}

		t = Game.objects.create(**game_data)
		return JsonResponse(serialize_game(t), status=201)

	def get(self, request):
		games = Game.objects.all()
		games_data = []
		for t in games:
			games_data.append(serialize_game(t))
		data = {
			'games': games_data,
			'count': games.count(),
		}
		return JsonResponse(data)

#games/<int:game_id>
class GameDetail(View):
	def get(self, request, game_id):
		try:
			t = Game.objects.get(pk=game_id)
		except Game.DoesNotExist:
			raise Http404()
		return JsonResponse({'game': serialize_game(t)})

	# allow only update of title and description
	def patch(self, request, game_id):
		try:
			data = json.loads(request.body.decode("utf-8"))
			t = Game.objects.get(pk=game_id)
			if (data.get('title')):
				t.title = data.get('title')
			if (data.get('description')):
				t.description = data.get('description')
			t.updated_at = datetime.datetime.now()
			t.save()

			return JsonResponse(serialize_game(t), status=200, safe=False)
		except Game.DoesNotExist:
			raise Http404()

	def delete(self, request, game_id):
		try:
			t = Game.objects.get(pk=game_id)
			t.delete();
			return JsonResponse({}, status=202)
		except Game.DoesNotExist:
			raise Http404()

