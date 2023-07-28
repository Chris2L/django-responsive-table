from django.shortcuts import render

# Create your views here.


# ----------  Data Subjects ---------

def index(request):
    return render(request, "index.html")