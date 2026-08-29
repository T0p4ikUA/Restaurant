from django import forms

from catalog.models import Position, Employee, Dish, Order


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name", "class": "form-control"}
        ),
    )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("position", "username", "is_active")


class EmployeeSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username",
                   "class": "form-control"}
        ),
    )


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("dish_name", "price", "cooked_by", "description")


class DishSearchForm(forms.Form):
    dish_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name of dish",
                   "class": "form-control"}
        ),
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "dishes",
            "order_taker",
            "customer_name",
            "table_number",
            "price"
        )


class OrderSearchForm(forms.Form):
    customer_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by customer name",
                   "class": "form-control"}
        ),
    )
