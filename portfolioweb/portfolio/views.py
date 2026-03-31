from django.shortcuts import render
from .models import Project
from  infoPersonal.models import Information

# Create your views here.
def portfolio(request):
    projects = Project.objects.all().order_by('-created')
    information = Information.objects.first()
    return render(request, "portfolio/portfolio.html", {'projects':projects, 'information': information,})

def contact(request):
    information = Information.objects.first()
    return render(request, "infoPersonal/contact.html", {'information':information})
