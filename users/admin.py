from django.contrib import admin
from .models import User, UserList, ListType


class ListInline(admin.TabularInline):
    fields = (
        'game',
        'type',
        'rate'
    )
    model = UserList
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = (ListInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'date_joined',
        'is_staff',
    )


class ListTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

admin.site.register(User, UserAdmin)
admin.site.register(ListType, ListTypeAdmin)