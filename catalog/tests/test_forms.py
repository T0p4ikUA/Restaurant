from django.test import TestCase

from catalog.forms import DishForm, EmployeeForm, OrderForm, PositionForm
from catalog.models import Dish, Employee, Position


class FormsTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Waiter")
        self.employee = Employee.objects.create_user(
            username="test_taker",
            password="securepassword123",
            position=self.position,
        )

        self.dish = Dish.objects.create(
            dish_name="soup",
            price=10.00,
        )

        self.dish_data = {
            "dish_name": "soup",
            "price": 10.00,
            "description": "A soup",
        }
        self.position_data = {
            "name": "Manager",
        }
        self.employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "password": "securepassword123",
            "username": "Jo123",
            "position": self.position.id,
        }
        self.order_data = {
            "customer_name": "customer123",
            "table_number": "12",
            "price": 20,
            "dishes": [self.dish.id],
            "order_taker": self.employee.id,
        }

    def test_position_is_valid(self):
        form = PositionForm(data=self.position_data)
        self.assertTrue(form.is_valid())

    def test_employee_is_valid(self):
        form = EmployeeForm(data=self.employee_data)
        self.assertTrue(form.is_valid())

    def test_dish_is_valid(self):
        form = DishForm(data=self.dish_data)
        self.assertTrue(form.is_valid())

    def test_order_is_valid(self):
        form = OrderForm(data=self.order_data)
        self.assertTrue(form.is_valid())

    def test_negative_price(self):
        dish_data = {
            "dish_name": "soup",
            "price": -1,
            "description": "A soup",
        }
        order_data = {
            "customer_name": "customer123",
            "table_number": "12",
            "price": -1,
            "dishes": [self.dish.id],
            "order_taker": self.employee.id,
        }
        form1 = DishForm(data=dish_data)
        form2 = OrderForm(data=order_data)
        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertIn("price", form1.errors)
        self.assertIn("price", form2.errors)

    def test_dish_form_missing_required_fields(self):
        form = DishForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("dish_name", form.errors)
        self.assertIn("price", form.errors)

    def test_order_form_missing_required_fields(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("table_number", form.errors)
        self.assertIn("price", form.errors)
        self.assertIn("customer_name", form.errors)
        self.assertIn("dishes", form.errors)
        self.assertIn("order_taker", form.errors)

    def test_position_form_missing_required_fields(self):
        form = PositionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_employee_form_missing_required_fields(self):
        form = EmployeeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("position", form.errors)
