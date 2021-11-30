from django.views.generic import ListView
from . import models
from django.shortcuts import render
# Create your views here.


class HomeView(ListView):
    """HomeView Defination"""
    model = models.Photo
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    context_object_name = "photos"


def photos_detail(request, pk):
    # pk not important pk가 potatoㄷ 될수 있음
    return render(request, "photos/detail.html")
