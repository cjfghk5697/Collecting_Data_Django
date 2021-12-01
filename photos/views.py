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
    cat_name = request.GET.get("cat_name", "Anycat")
    cat_name = str.capitalize(cat_name)

    filter_args = {}
    form = {
        "cat_name": cat_name,
    }

    if cat_name != "Anycat":
        filter_args["cat_name"] = cat_name
    photos = models.Photo.objects.filter(**filter_args)

    return render(request, "photos/search.html", {**form, "photos": photo1})
