import django_tables2 as tables

from .models import Author


class AuthorTable(tables.Table):
    class Meta:
        model = Author
        template_name = "common/django_tables2.html"

    # @classmethod
    # def render_paginated_table(cls, request):
    #     """Render paginated table"""
    #     table = cls(data=Author.objects.all())
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    #     return table