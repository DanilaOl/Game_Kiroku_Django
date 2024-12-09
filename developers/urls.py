from django.urls import path

from . import views

app_name = 'developers'

urlpatterns = [
    path('', views.DeveloperListView.as_view(), name='developer_list'),
    path('<int:pk>/', views.DeveloperDetailView.as_view(), name='developer_detail'),
]