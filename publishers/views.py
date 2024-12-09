from django.views.generic import ListView, DetailView
from .models import Publisher
from mixins.filter_form_mixin import FilterFormMixin


class PublisherListView(FilterFormMixin, ListView):
    model = Publisher
    paginate_by = 20
    ordering = 'name'


class PublisherDetailView(FilterFormMixin, DetailView):
    model = Publisher
