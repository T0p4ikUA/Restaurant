from time import sleep
from django.test import TestCase

from catalog.models import Position, Employee, Order, Dish


class ModelsTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.employee = Employee.objects.create(
            username="bob123",
            position=self.position,
        )
        self.dish = Dish.objects.create(
            dish_name="soup",
            price=10.00,
        )
        self.order_data = {
            "customer_name": "customer123",
            "table_number": "12",
            "price": 20,
            "order_taker": self.employee,
        }

    def test_position_format_str(self):
        position = Position.objects.create(name="Director")
        self.assertEqual(
            str(position), position.name
        )

    def test_employee_format_str(self):
        employee = Employee.objects.create(
            username="alice123",
            position=self.position
        )
        self.assertEqual(
            str(employee),
            f"{employee.username} (position: {employee.position})"
        )

    def test_order_format_str(self):
        order = Order.objects.create(**self.order_data)
        order.dishes.set([self.dish])
        self.assertEqual(
            str(order),
            f"{order.customer_name} (Table: {order.table_number})"
        )

    def test_dish_order_format_str(self):
        self.assertEqual(
            str(self.dish),
            f"{self.dish.dish_name} (${self.dish.price})"
        )

    def test_order_ordering(self):
        order1 = Order.objects.create(**self.order_data)
        order1.dishes.set([self.dish])
        sleep(0.01)
        order2 = Order.objects.create(
            customer_name="Bob",
            table_number="2",
            price=20,
            order_taker=self.employee
        )
        order2.dishes.set([self.dish])
        orders = Order.objects.all()
        self.assertEqual(list(orders), [order2, order1])

    def test_employee_ordering(self):
        Employee.objects.filter(username__in=["zack", "john"]).delete()
        emp1 = Employee.objects.create(
            username="zack", position=self.position
        )
        emp2 = Employee.objects.create(
            username="john", position=self.position
        )
        employees = Employee.objects.filter(username__in=["zack", "john"])
        self.assertEqual(list(employees), [emp2, emp1])

    def test_dish_order_ordering(self):
        Dish.objects.filter(dish_name__in=["soup", "salad"]).delete()
        dish1 = Dish.objects.create(dish_name="soup", price=10.00)
        dish2 = Dish.objects.create(dish_name="salad", price=5.00)
        dishes = Dish.objects.filter(dish_name__in=["soup", "salad"])
        self.assertEqual(list(dishes), [dish2, dish1])

    def test_position_ordering(self):
        Order.objects.all().delete()
        Employee.objects.all().delete()
        Position.objects.all().delete()

        position1 = Position.objects.create(
            name="Manager",
        )
        position2 = Position.objects.create(
            name="Waiter",
        )
        positions = Position.objects.all()
        self.assertEqual(list(positions), [position1, position2])
