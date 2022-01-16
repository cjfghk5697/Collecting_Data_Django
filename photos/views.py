from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Photo, File


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


def create(request):

    if(request.method == 'POST'):

        post = Photo()
        post.cat_name = request.POST['cat_name']
        post.description = request.POST['description']
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다

        # Photo 객체를 하나 생성한다.
        photo = File()
        # 외래키로 현재 생성한 Post의 기본키를 참조한다.
        photo.photo = post
        # imgs로부터 가져온 이미지 파일 하나를 저장한다.
        photo.file = request.FILES['imgs']
        # 데이터베이스에 저장
        photo.save()

    return render(request, 'photos/upload.html')
