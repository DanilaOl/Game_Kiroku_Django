from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.GamesListView.as_view(), name='games_list'),
    path('<int:pk>/', views.GameDetailView.as_view(), name='games_detail'),
]