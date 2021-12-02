from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms


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


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            cat = form.cleaned_data.get("cat")
            filter_args = {}

            if cat != "Anywhere":
                filter_args["cat__startswith"] = cat
            photos = models.Photo.objects.filter(**filter_args)
        else:
            form = forms.SearchForm()

        return render(request, "photos/search.html", {"form": form, "photos": photos})
