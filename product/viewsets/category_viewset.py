from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import Category
from product.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
