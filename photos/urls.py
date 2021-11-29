from django.urls import path
from . import views

app_name = "photos"
('ROUTE/', VIEW.as_view(), name=''),


urlpatterns = [
    path("<int:pk>", include("views.photos_detail", name="photos")),
]
