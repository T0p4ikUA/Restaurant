from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Employee(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username} (position: {self.position.name})"


class Dish(models.Model):
    dish_name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    cooked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="dishes",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("dish_name",)

    def __str__(self) -> str:
        return f"{self.dish_name} (${self.price})"


class Order(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
    order_taker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    customer_name = models.CharField(max_length=255)
    table_number = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.customer_name} (Table: {self.table_number})"
