from time import sleep
from django.test import TestCase

from catalog.models import Position, Employee, Order, Dish


class ModelsTest(TestCase):
    def setUp(self):
        self.position_data = {
            "name": "Manager",
        }
        self.position = Position.objects.create(
            **self.position_data
        )

        self.dish_data = {
            "dish_name": "soup",
            "price": 10.00,
        }
        self.employee_data = {
            "username": "bob123",
            "position": self.position,
        }
        self.order_data = {
            "customer_name": "customer123",
            "table_number": "12",
            "price": 20,
        }

    def test_position_format_str(self):
        position = Position.objects.create(name="Director")
        self.assertEqual(
            str(position), position.name
        )

    def test_employee_format_str(self):
        employee = Employee.objects.create(
            **self.employee_data
        )
        self.assertEqual(
            str(employee),
            f"{employee.username} (position: {employee.position})"
        )

    def test_order_format_str(self):
        order = Order.objects.create(
            **self.order_data
        )
        self.assertEqual(
            str(order),
            f"{order.customer_name} ({order.table_number})"
        )

    def test_dish_order_format_str(self):
        dish = Dish.objects.create(
            **self.dish_data
        )
        self.assertEqual(
            str(dish),
            f"{dish.dish_name} (${dish.price})"
        )

    def test_order_ordering(self):
        order1 = Order.objects.create(
            **self.order_data
        )
        sleep(0.01)
        order2 = Order.objects.create(
            customer_name="Bob",
            table_number="2",
            price=20
        )
        orders = Order.objects.all()
        self.assertEqual(list(orders), [order2, order1])

    def test_employee_ordering(self):
        Employee.objects.all().delete()
        emp1 = Employee.objects.create(username="zack", position=self.position)
        emp2 = Employee.objects.create(username="john", position=self.position)
        employees = Employee.objects.all()
        self.assertEqual(list(employees), [emp2, emp1])

    def test_dish_order_ordering(self):
        Dish.objects.all().delete()
        dish1 = Dish.objects.create(dish_name="soup", price=10.00)
        dish2 = Dish.objects.create(dish_name="salad", price=5.00)
        dishes = Dish.objects.all()
        self.assertEqual(list(dishes), [dish2, dish1])

    def test_position_ordering(self):
        Position.objects.all().delete()
        position1 = Position.objects.create(
            name="Manager",
        )
        position2 = Position.objects.create(
            name="Waiter",
        )
        positions = Position.objects.all()
        self.assertEqual(list(positions), [position1, position2])
