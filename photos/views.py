from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):
    """HomeView Defination"""
    model = models.Photo
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    context_object_name = "photos"


class PhotoDetail(DetailView):
    """PhotoDetail Definition"""
    model = models.Photo


def search(request):
    cat = request.GET.get("cat")
    cat = str.capitalize(cat)
    return render(request, "photos/search.html", {"cat": cat})
