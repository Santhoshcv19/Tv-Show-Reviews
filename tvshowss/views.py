from django.shortcuts import render
from django.http import HttpResponse
from .models import reviews

def home(request):
    projects = reviews.objects.order_by('-title')[:5]
    return render(request, 'tvshowss/home.html', {'projects':projects})
