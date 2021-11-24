from django.urls import path
from photos import views as photo_views

app_name = "core"

urlpatterns = [path("", photo_views.all_cats, name="cats")]
