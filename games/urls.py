from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.GamesListView.as_view(), name='game_list'),
    path('<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('<int:pk>/update_list', views.update_list, name='update_list'),
    path('<int:pk>/create_comment', views.create_comment, name='create_comment'),
    path('<int:pk>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]