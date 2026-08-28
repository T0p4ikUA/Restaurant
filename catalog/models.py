from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} (position: {self.position})"


class Dish(models.Model):
    dish_name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    description = models.TextField(null=True, blank=True)
    cooked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="dishes",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("dish_name",)

    def __str__(self):
        return f"{self.dish_name} (${self.price})"


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    table_number = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    dishes = models.ManyToManyField(
        Dish,
        related_name="orders",
        blank=True,
    )
    order_taker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.customer_name} ({self.table_number})"
