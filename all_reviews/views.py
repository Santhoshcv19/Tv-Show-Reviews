from django.shortcuts import render
from .models import alls

def all(request):
    revs=alls.objects.order_by('-title')
    return render(request, 'all_reviews/all.html',{'revs':revs})
