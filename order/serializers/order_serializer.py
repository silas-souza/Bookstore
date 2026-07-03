from rest_framework import serializers
from order.models import Order
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    # Aqui trazemos os detalhes dos produtos que estão na Order
    product = ProductSerializer(read_only=True, many=True)
    
    class Meta:
        model = Order
        fields = '__all__'