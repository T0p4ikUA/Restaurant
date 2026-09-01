from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Position, Dish


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Manager")
        self.admin_user = (
            get_user_model().objects.create_superuser(
                username="admin",
                password="testadmin123",
                position=self.position
            )
        )
        self.client.force_login(self.admin_user)
        self.dish = Dish.objects.create(
            dish_name="soup",
            description="taste soup",
            price=10.00,
        )

    def test_admin_list_add_and_pages(self):
        for action in ["changelist", "add"]:
            with self.subTest(action=action):
                url = reverse(f"admin:catalog_position_{action}")
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_admin_change_and_delete(self):
        for action in ["change", "delete"]:
            with self.subTest(action=action):
                url = reverse(
                    f"admin:catalog_position_{action}",
                    args=[self.position.id]
                )
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_dish_description(self):
        url = reverse("admin:catalog_dish_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dish.description)
