from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist, \
    PermissionDenied
from django.db import models
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from mixins.filter_form_mixin import FilterFormMixin
from users.forms import UserListForm
from users.models import UserList
from .forms import GameFilterForm, CommentForm
from .models import Game, Comment


def index(request):
    return redirect('games:game_list', permanent=True)


class GamesListView(FilterFormMixin, ListView):
    model = Game
    paginate_by = 10
    ordering = 'id'

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

    def get_queryset(self):
        qs = super(GameDetailView, self).get_queryset()
        qs = qs.select_related('developer', 'publisher')
        return qs

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            return context

        instance = UserList.objects.filter(user=self.request.user,
                                           game=context['object'])
        try:
            instance = instance.get()
        except ObjectDoesNotExist:
            instance = None

        user_list_form_initial = {
            'user': self.request.user,
            'game': context['object'],
            'rate': None,
        }

        user_list_form = UserListForm(instance=instance, initial=user_list_form_initial)
        context['user_list_form'] = user_list_form

        comment_form_initial = {
            'user': self.request.user,
            'game': context['object'],
        }
        comment_form = CommentForm(initial=comment_form_initial)
        context['comment_form'] = comment_form

        return context

@login_required
def update_list(request, pk):
    if request.method != 'POST':
        return redirect('games:game_detail', pk=pk)

    try:
        instance = UserList.objects.get(user=request.user, game=pk)
    except ObjectDoesNotExist:
        instance = None

    user_list_form = UserListForm(request.POST, instance=instance)

    if not user_list_form.is_valid():
        raise ValidationError(user_list_form.errors)

    if user_list_form.instance.type.type == 'delete':
        user_list_form.instance.delete()
        user_list_form.instance.game.recalculate_rating()
        return redirect('games:game_detail', pk=pk)

    if not instance:
        user_list_form.instance.game = Game.objects.get(pk=pk)
        user_list_form.instance.user = request.user

    user_list_form.save()
    user_list_form.instance.game.recalculate_rating()

    return redirect('games:game_detail', pk=pk)

@login_required
def create_comment(request, pk):
    if request.method != 'POST':
        return redirect('games:game_detail', pk=pk)

    comment_form = CommentForm(request.POST)

    if not comment_form.is_valid():
        raise ValidationError(comment_form.errors)

    comment_form.instance.user = request.user
    comment_form.instance.game = Game.objects.get(pk=pk)
    comment_form.save()

    return redirect('games:game_detail', pk=pk)


@login_required
def delete_comment(request, pk, comment_id):
    if request.method != 'POST':
        return redirect('games:game_detail', pk=pk)

    instance = Comment.objects.get(pk=comment_id)
    if instance.user != request.user:
        raise PermissionDenied

    instance.delete()
    return redirect('games:game_detail', pk=pk)
