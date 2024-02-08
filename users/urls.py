from django.urls import path, include
from users.views import register_user_view, success_login
from rest_framework.authtoken import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    path("register/", register_user_view, name="register-user-view"),
    path("sucess_login/", success_login, name="sucess-login"),
]