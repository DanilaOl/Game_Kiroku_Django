from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import User, UserList
from games.views import FilterFormMixin

class UserDetailView(FilterFormMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)

        lists = UserList.objects.filter(user=context['object'])
        lists_grouped: dict[str, list] = {}

        for user_list in lists:
            if lists_grouped.get(user_list.type.type):
                lists_grouped[user_list.type.type].append(user_list)
            else:
                lists_grouped[user_list.type.type] = [user_list]

        context['lists_grouped'] = lists_grouped
        return context


@login_required(login_url='login')
def current_user_redirect(request):
    return redirect('users:user_detail', pk=request.user.id)
