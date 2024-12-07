from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.current_user_redirect, name='current_user_redirect'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]