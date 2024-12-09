from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserList, ListType, User


class UserListForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=ListType.objects.order_by('order'), label='Тип списка')
    class Meta:
        model = UserList
        fields = '__all__'

        choices = [(None, 'Нет')] + [(i, i) for i in range(1, 11)]
        widgets = {
            'type': forms.Select,
            'rate': forms.Select(choices=choices),
            'user': forms.HiddenInput,
            'game': forms.HiddenInput,
        }



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')