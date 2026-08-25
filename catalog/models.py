from django.contrib.auth.models import AbstractUser
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
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
        return (f"{self.username}, "
                f"(is_active: {self.is_active},"
                f"position: {self.position})")
