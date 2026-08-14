"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# bookstore/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicione a linha abaixo para registrar as rotas da sua API:
    path('api/v1/', include('product.urls')),
    # Ou se quiser sem o prefixo api/v1/:
    # path('', include('product.urls')),
]
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Bookstore!</h1><p>Acesse <a href='/admin/'>/admin/</a> ou <a href='/api/v1/product/'>/api/v1/product/</a></p>")

urlpatterns = [
    path('', home),  # <-- ADICIONA ESTA LINHA
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
]
