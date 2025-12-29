from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product


class ProductCreateTest(APITestCase):

    def test_create_product_success(self):
        url = reverse('product-list')

        data = {
            "name": "Laptop",
            "description": "Gaming Laptop",
            "price": 75000,
            "stock_quantity": 10,
            "category": "Electronics"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProductFetchTest(APITestCase):

    def setUp(self):
        Product.objects.create(
            name="Phone",
            description="Smartphone",
            price=30000,
            stock_quantity=5,
            category="Electronics"
        )

    def test_get_product_list(self):
        response = self.client.get("/api/v1/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        product = Product.objects.first()
        response = self.client.get(f"/api/v1/products/{product.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Phone")


class ProductUpdateTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Tablet",
            description="Android Tablet",
            price=20000,
            stock_quantity=3,
            category="Tech"
        )

    def test_update_product(self):
        data = {
            "name": "Tablet Pro",
            "description": "Updated version",
            "price": 25000,
            "stock_quantity": 4,
            "category": "Tech"
        }

        response = self.client.put(
            f"/api/v1/products/{self.product.id}/", data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Tablet Pro")


class ProductDeleteTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Headphones",
            description="Noise cancelling",
            price=5000,
            stock_quantity=7,
            category="Electronics"
        )

    def test_delete_product(self):
        response = self.client.delete(f"/api/v1/products/{self.product.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
