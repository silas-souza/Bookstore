"""bookstore URL Configuration"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from bookstore import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("api/v1/", include("product.urls")),
    path("api/v1/", include("order.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
