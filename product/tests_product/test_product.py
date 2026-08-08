from rest_framework.test import APITestCase
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

class ProductAndCategoryTests(APITestCase):

    def setUp(self):
        # Corrigido para 'name' baseado no seu Model
        self.category = Category.objects.create(name="Livros", description="Todos os livros")
        self.product = Product.objects.create(
            name="Dune", 
            price=49.90, 
            category=self.category
        )

    def test_category_serializer_integrity(self):
        """Valida o serializer de Categoria"""
        serializer = CategorySerializer(self.category)
        self.assertEqual(serializer.data['name'], "Livros")

    def test_product_serializer_integrity(self):
        """Valida o serializer de Produto"""
        serializer = ProductSerializer(self.product)
        self.assertEqual(serializer.data['name'], "Dune")