from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
