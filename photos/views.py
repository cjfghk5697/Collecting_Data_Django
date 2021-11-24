from django.shortcuts import render
from datetime import datetime
# Create your views here.


def all_cats(request):
    now = datetime.now()
    hungry = False
    return render(request, "input.html", context={
        'now': now,
        'hungry': hungry
    })
