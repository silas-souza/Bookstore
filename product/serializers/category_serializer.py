from rest_framework import serializers
from product.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
    
    extra_kwargs = {'slug':{'required':False}}