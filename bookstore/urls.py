"""
URL configuration for bookstore project.
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.viewsets import ProductViewSet, CategoryViewSet
from order.viewsets import OrderViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
