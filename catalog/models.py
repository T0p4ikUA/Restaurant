from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} (position: {self.position})"


class Dish(models.Model):
    dish_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cooked_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ["dish_name"]

    def __str__(self):
        return f"{self.dish_name} (${self.price})"


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    table_number = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    dishes = models.ManyToManyField(Dish, related_name="orders")
    order_taker = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} (Table: {self.table_number})"
