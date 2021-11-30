from django.views.generic import ListView
from . import models
from django.shortcuts import render, redirect
from django.db.models import ObjectDoesNotExist
from django.urls import reverse
from django.http import Http404


class HomeView(ListView):
    """HomeView Defination"""
    model = models.Photo
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    context_object_name = "photos"


def photos_detail(request, pk):
    # pk not important pk가 potatoㄷ 될수 있음
    try:
        photo = models.Photo.objects.get(pk=pk)
        return render(request, "photos/detail.html", {'photo': photo})
    except models.Photo.DoesNotExist:
        raise Http404()
