from django import forms
from .models import Game, Comment


class GameFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GameFilterForm, self).__init__(*args, **kwargs)
        self.fields['developer'].required = False
        self.fields['publisher'].required = False
        self.fields['genres'].required = False

    class Meta:
        model = Game
        fields = ('developer', 'publisher', 'genres')
        widgets = {
            'developer': forms.Select,
            'publisher': forms.Select,
            'genres': forms.SelectMultiple,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
