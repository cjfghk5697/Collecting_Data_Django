from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("sigup", views.SignUpView.as_view(), name="signup"),
    path("logout", views.log_out, name="logout"),
    path("login", views.LoginView.as_view(), name="login")]
