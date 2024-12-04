from django.contrib import admin

from .models import Developer
from games.models import Game


class GameInline(admin.TabularInline):
    model = Game
    extra = 0
    fields = (
        'name',
        'release_date',
        'rating',
        'publisher',

    )
    readonly_fields = fields
    show_change_link = True


# Register your models here.
class DeveloperAdmin(admin.ModelAdmin):
    inlines = (GameInline,)
    list_display = (
        'name',
        'country'
    )

admin.site.register(Developer, DeveloperAdmin)
admin.site.empty_value_display = 'Нет'