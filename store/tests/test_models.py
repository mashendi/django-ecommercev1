from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        data = self.data1
        self.assertIsInstance(data, Category)

    def test_category_model_return(self):
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1, title="django beginner", slug="django-beginner",
            price="20.00", created_by_id=1, image="django")

    def test_product_model_entry(self):
        data = self.data1
        self.assertIsInstance(data, Product)

    def test_product_model_return(self):
        data = self.data1
        self.assertEqual(str(data), "django beginner")
