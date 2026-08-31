from rest_framework.test import APITestCase
from product.models import Product, Category
from order.models import Order
from order.serializers import OrderSerializer


class OrderTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Ficção",
            description="Livros de ficção"
        )

        self.product = Product.objects.create(
            name="Neuromancer",
            price=55.00,
            category=self.category
        )

        self.order = Order.objects.create(
            product=self.product,
            quantity=2,
            total_price=110.00
        )

    def test_order_serializer_integrity(self):
        """Valida o serializer de Pedido e sua relação com produto."""
        serializer = OrderSerializer(self.order)

        self.assertEqual(serializer.data["product"], self.product.id)
        self.assertEqual(serializer.data["product_name"], "Neuromancer")
        self.assertEqual(serializer.data["quantity"], 2)
        self.assertEqual(str(serializer.data["total_price"]), "110.00")