from django.urls import path

from . import views

app_name = 'publishers'

urlpatterns = [
    path('', views.PublisherListView.as_view(), name='publisher_list'),
    path('<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail'),
]