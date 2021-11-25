from django.core import paginator
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
# Create your views here.


def all_cats(request):
    page = request.GET.get("page", 1)
    cat_list = models.Photo.objects.all()
    paginator = Paginator(cat_list, 10, orphans=5)
    cats = paginator.get_page(int(page))

    return render(request, "input.html", context={
        "page": cats
    })
