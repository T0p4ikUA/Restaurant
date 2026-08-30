from django import forms
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.db import models

from catalog.models import Employee, Position, Dish, Order


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info",
         {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                )
            },
        ),
    )
    list_filter = ["position"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["dish_name", "price", "cooked_by", "description"]
    list_filter = ["cooked_by"]
    search_fields = ["dish_name"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "customer_name",
        "table_number",
        "price",
        "created_at",
        "dishes",
        "order_taker",
    ]
    list_filter = ["created_at", "order_taker"]
    search_fields = ["customer_name", "table_number"]
    formfield_overrides = {
        models.ManyToManyField: {"widget": forms.CheckboxSelectMultiple},
    }

    @admin.display(description="dishes")
    def dishes(self, obj):
        return ", ".join([dish.dish_name for dish in obj.dishes.all()])
