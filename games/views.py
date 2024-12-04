from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Comment, Genre
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('games:catalog', permanent=True)


def catalog(request):
    all_games = Game.objects.all()
    return render(request, 'games/catalog.html')


def game(request, game_id):
    game_obj = get_object_or_404(Game, pk=game_id)
    # messages.success(request, 'works')
    return HttpResponse(game_obj, request.user)
