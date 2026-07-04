import factory
from factory.django import DjangoModelFactory
from product.models import Category, Product

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=100)

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    stock = factory.Faker('random_int', min=0, max=100)
    category = factory.SubFactory(CategoryFactory)
