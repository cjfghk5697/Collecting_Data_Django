from django.core import paginator
from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


def all_cats(request):
    page = request.GET.get("page", 1)
    cat_list = models.Photo.objects.all()
    paginator = Paginator(cat_list, 10, orphans=5)
    try:
        cats = paginator.page(int(page))
        return render(request, "input.html", context={"page": cats})
    except EmptyPage:
        return redirect("/")
