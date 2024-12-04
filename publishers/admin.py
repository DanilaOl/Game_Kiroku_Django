from django.contrib import admin

from publishers.models import Publisher
from games.models import Game

class GameInline(admin.TabularInline):
    model = Game
    extra = 0
    fields = (
        'name',
        'release_date',
        'rating',
        'developer',
    )
    readonly_fields = fields
    show_change_link = True


# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    inlines = (GameInline,)
    list_display = (
        'name',
        'country'
    )

admin.site.register(Publisher, PublisherAdmin)
admin.site.empty_value_display = 'Нет'
