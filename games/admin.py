from django.contrib import admin
from .models import Game, Genre, Comment


# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'release_date',
        'developer',
        'publisher',
    )
    list_editable = (
        'release_date',
        'developer',
        'publisher'
    )
    search_fields = ('name',)
    list_filter = ('developer', 'publisher', 'genres')
    list_display_links = ('name',)
    filter_horizontal = ('genres',)
    list_select_related = True


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name', )
    list_editable = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'game',
        'user',
        'text',
        'created_at'
    )
    list_display_links = ('pk',)
    search_fields = ('game__name', 'user__username')


admin.site.register(Game, GameAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.empty_value_display = 'Нет'
