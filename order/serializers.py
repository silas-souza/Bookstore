from rest_framework import serializers
from product.serializers import ProductSerializer
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price', 'created_at']
