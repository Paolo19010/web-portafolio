from django.shortcuts import render
from .models import Information, Background

# Create your views here.
def home(request):
    information = Information.objects.first()
    background, created = Background.objects.get_or_create(id=1)
    return render(request, "infoPersonal/home.html", {'information':information, 'background': background},)

def about(request):
    information = Information.objects.first()
    background = Background.objects.first()
    return render(request, "infoPersonal/about.html", {'information':information, 'background': background},)

def contact(request):
    information = Information.objects.first()
    background = Background.objects.first()
    return render(request, "infoPersonal/contact.html", {'information':information, 'background': background},)

