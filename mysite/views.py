from django.shortcuts import render
from django.http import HttpResponse
from .models import Testimony, Technology


# Create your views here.
def home(request):
    testimonies = Testimony.objects.filter(show=True)
    technoloies = Technology.objects.filter(show=True)
    return render(request, "home.html", {'testimonies': testimonies, 'technologies': technoloies}) 