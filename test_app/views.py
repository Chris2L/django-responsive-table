from django.core.management import call_command
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import AuthorFilter
from .models import Author
from .tables import AuthorTable


def index(request):
    authors = Author.objects.all()
    context = {
        "authors":authors
    }
    return render(request, "index.html", context)

def index_tables2(request):
    template_name = "index_tables2.html"
    if request.htmx:
        template_name = "htmx/table.html"
    context = {"table": AuthorTable.render_paginated_table(request)}
    return render(request, template_name, context)

class AuthorHTMxTableView(SingleTableMixin, FilterView):
    table_class = AuthorTable
    queryset = Author.objects.all()
    filterset_class = AuthorFilter
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            template_name = "htmx/table.html"
        else:
            template_name = "index_tables2.html"

        return template_name