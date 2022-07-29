from django.contrib import admin

from home.models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active')
    list_editable = ('active',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Users, UsersAdmin)
