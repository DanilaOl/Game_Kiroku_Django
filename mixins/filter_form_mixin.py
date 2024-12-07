from django.views.generic.base import ContextMixin, View
from games.forms import GameFilterForm


class FilterFormMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = GameFilterForm(self.request.GET or None)
        return context