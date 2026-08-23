from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    
    class Meta:
        model = Order
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price', 'created_at']
