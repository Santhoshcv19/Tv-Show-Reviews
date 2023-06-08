from django.shortcuts import render, get_object_or_404
from .models import alls

def all(request):
    revs=alls.objects.order_by('title')
    return render(request, 'all_reviews/all.html',{'revs':revs})

def detail(request, alls_id):
    als=get_object_or_404(alls, pk=alls_id)
    return render(request, 'all_reviews/detail.html',{'als':als})
