from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin, View

from .forms import GameFilterForm
from .models import Game


# Create your views here.

def index(request):
    return redirect('games:games_list', permanent=True)


class FilterFormMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = GameFilterForm(self.request.GET or None)
        return context


class GamesListView(FilterFormMixin, ListView):
    model = Game
    paginate_by = 10

    def get_queryset(self):
        qs = super(GamesListView, self).get_queryset()

        if not self.request.GET:
            return qs

        search = self.request.GET.get('search_text')
        filter_form = GameFilterForm(self.request.GET)

        if not filter_form.is_valid():
            raise ValidationError(filter_form.errors)

        filters = models.Q()

        if filter_form.cleaned_data['developer']:
            filters &= models.Q(
                developer=filter_form.cleaned_data['developer'])
        if filter_form.cleaned_data['publisher']:
            filters &= models.Q(
                publisher=filter_form.cleaned_data['publisher'])
        if filter_form.cleaned_data['genres']:
            filters &= models.Q(genres__in=filter_form.cleaned_data['genres'])
        if search:
            filters &= models.Q(name__icontains=search)

        return qs.filter(filters).distinct()


class GameDetailView(FilterFormMixin, DetailView):
    model = Game


