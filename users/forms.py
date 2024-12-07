from django import forms
from .models import UserList, ListType


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
