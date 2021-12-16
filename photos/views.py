from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


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

            filter_args["cat_name"] = cat_name

            photo1 = models.Photo.objects.filter(**filter_args)

            paginator = Paginator(photo1, 10, orphans=5)
            page = request.GET.get("page", 1)

            photos = paginator.get_page(page)
            return render(request, "photos/search.html", {"form": form, "photos": photos})
        else:

            form = forms.SearchForm()
        return render(request, "photos/search.html", {"form": form})


class UploadView(FormView):
    template_name = "photos/upload.html"
    form_class = forms.FileUploadForm

    success_url = reverse_lazy("core:cats")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
