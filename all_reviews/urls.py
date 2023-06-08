from django.urls import path,include
from . import views

app_name='all_reviews'

urlpatterns = [
    path('',views.all, name='all'),
]