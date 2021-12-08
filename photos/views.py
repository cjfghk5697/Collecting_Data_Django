from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms


class HomeView(ListView):
    """HomeView Defination"""
    model = models.Photo
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "photos"


class PhotoDetail(DetailView):
    """PhotoDetail Definition"""
    model = models.Photo


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            cat_name = form.cleaned_data.get("cat_name")
            filter_args = {}

            filter_args["cat_name__startswith"] = cat_name

            photo1 = models.Photo.objects.filter(**filter_args)

            return render(request, "photos/search.html", {"form": form, "photo1": photo1})
        else:

            form = forms.SearchForm()
            return render(request, "photos/search.html", {"form": form})
