from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def all_cats(request):
    return HttpResponse(content="hello world")
