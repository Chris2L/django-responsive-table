from django import forms
from django.contrib.auth.models import User

from .models import Author

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.db.models import Q
                

class AuthorForm(forms.ModelForm):
    # required_css_class = 'form-control required'
    # error_css_class = "form-control is-invalid"
    # template_name = "forms/custom_form_template.html"

    class Meta:
        model = Author

        fields = (
            'name',
            'lastname',
            'country',
            'email',
            'still_alive'
        )
