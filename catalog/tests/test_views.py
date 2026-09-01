from django.test import TestCase
from django.urls import reverse
from catalog.models import Position, Employee, Order


class ViewsTest(TestCase):
    def setUp(self):
        position = Position.objects.create(
            name="Manager"
        )
        self.employee = Employee.objects.create(
            username="bob123",
            position=position
        )

    def test_is_logged_user_have_access(self):
        self.client.force_login(self.employee)
        response = self.client.get(reverse("catalog:order-list"))
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_have_access(self):
        self.client.force_login(self.employee)
        self.client.logout()
        response = self.client.get(reverse("catalog:order-list"))
        self.assertEqual(response.status_code, 302)
        login_url = reverse("catalog:login") if "catalog:login" in [r.name for r in reverse.__globals__.get('urlresolver', [])] else "/accounts/login/"
        order_list_url = reverse("catalog:order-list")
        self.assertRedirects(
            response,
            f"{login_url}?next={order_list_url}"
        )

    def test_pagination(self):
        self.client.force_login(self.employee)
        for i in range(12):
            Order.objects.create(
                customer_name=f"Customer {i}",
                table_number=str(i),
                price=10,
                order_taker=self.employee
            )
        response = self.client.get(reverse("catalog:order-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["orders_list"]), 3)
