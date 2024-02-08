from django.urls import path, include
from users.views import register_user_view, success_login


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", register_user_view, name="register-user-view"),
    path("sucess_login/", success_login, name="sucess-login"),
]