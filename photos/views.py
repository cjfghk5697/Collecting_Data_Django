from django.shortcuts import render
from datetime import datetime
from . import models
# Create your views here.


def all_cats(request):

    now = datetime.now()
    count_cats = models.Photo.objects.all().count()
    all_cats = models.File.objects.all()

    return render(request, "input.html", context={
        'now': now,
        'all_cats': all_cats,
        'count_cats': count_cats,
    })
