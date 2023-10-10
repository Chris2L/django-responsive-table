from decimal import Decimal

import django_filters
from django import forms
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Author


class AuthorFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="", widget=forms.TextInput(attrs={'class':"form-inline", 'hx-get':reverse_lazy("home2"),
                'hx-target':'#tableContainer',
        'hx-swap':"outerHTML",
        'hx-indicator':".progress",
        'hx-trigger':"keyup changed delay:500ms, search" }))

    class Meta:
        model = Author
        fields = ['query']
        # form = AuthorFilterForm

    def universal_search(self, queryset, name, value):
        return Author.objects.filter(
            Q(name__icontains=value) | Q(lastname__icontains=value) | Q(country__icontains=value)
        )