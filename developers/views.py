from django.views.generic import ListView, DetailView

from .models import Developer
from mixins.filter_form_mixin import FilterFormMixin


class DeveloperListView(FilterFormMixin, ListView):
    model = Developer
    paginate_by = 20
    ordering = 'name'


class DeveloperDetailView(FilterFormMixin, DetailView):
    model = Developer

