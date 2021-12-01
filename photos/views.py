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
    cat = request.GET.get("cat", "Anycat")
    cat = str.capitalize(cat)

    filter_args = {}
    form = {
        "cat": cat,
    }

    if cat != "Anycat":
        filter_args["cat__startswith"] = cat
    photos = models.Photo.objects.filter(**filter_args)

    return render(request, "photos/search.html", {**form, "photos": photos})
