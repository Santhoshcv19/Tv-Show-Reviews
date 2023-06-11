from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import reviews

def home(request):
    projects = reviews.objects.order_by('-title')[:3]
    return render(request, 'tvshowss/home.html', {'projects':projects})