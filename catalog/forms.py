from django import forms

from catalog.models import Position, Employee, Dish


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("position", "username", "is_active")


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("dish_name", "price", "cooked_by", "description")