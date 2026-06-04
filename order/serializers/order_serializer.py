from rest_framework import serializers
from order.models import Order
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'products', 'user', 'total', 'created_at']
        read_only_fields = ['id', 'total', 'created_at']
    
    def get_total(self, obj):
        return sum([product.price for product in obj.product.all()])
