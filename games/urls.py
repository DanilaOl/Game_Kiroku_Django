from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:game_id>/', views.game, name='game'),
]