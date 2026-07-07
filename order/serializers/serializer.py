from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # Mostra os detalhes da categoria ao listar o produto (opcional)
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'category_detail']


class OrderSerializer(serializers.ModelSerializer):
    # Exibe a lista de IDs dos produtos pertencentes ao pedido
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'status', 'products', 'total_value']
        read_only_fields = ['total_value']  # Geralmente calculado automaticamente