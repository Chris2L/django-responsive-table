from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        "authors":authors
    }
    return render(request, "index.html", context)