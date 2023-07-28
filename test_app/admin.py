from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'lastname',
        'country',
        'email',
        'still_alive',
    )
    list_filter = ('still_alive',)
    search_fields = ('name',)