from rest_framework.test import APITestCase
from django.contrib.auth.models import User  # 👈 Importa o modelo de usuário do Django
from product.models import Product, Category
from order.models import Order
from order.serializers import OrderSerializer

class OrderTests(APITestCase):

    def setUp(self):
        # 1. Cria a categoria e o produto
        self.category = Category.objects.create(name="Ficção")
        self.product = Product.objects.create(name="Neuromancer", price=55.00, category=self.category)
        
        # 2. Cria um usuário fictício para o teste
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # 3. Cria a order passando o usuário obrigatório (user=self.user)
        self.order = Order.objects.create(user=self.user)
        
        # 4. Adiciona o produto na relação ManyToMany do pedido
        self.order.product.add(self.product) 

    def test_order_serializer_integrity(self):
        """Valida o serializer de Pedido e sua relação com produtos"""
        serializer = OrderSerializer(self.order)
        self.assertEqual(len(serializer.data['product']), 1)
        self.assertEqual(serializer.data['product'][0]['name'], "Neuromancer")