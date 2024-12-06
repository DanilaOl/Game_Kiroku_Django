from django.shortcuts import render
from django.views.generic import DetailView
from .models import User
from games.views import FilterFormMixin

class UserDetailView(FilterFormMixin, DetailView):
    model = User

