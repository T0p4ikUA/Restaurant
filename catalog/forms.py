from django import forms

from catalog.models import Dish, Employee, Order, Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ("name",)


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control"
            }
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
            attrs={
                "placeholder": "Search by username",
                "class": "form-control"
            }
        ),
    )


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("dish_name", "price", "cooked_by", "description")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price


class DishSearchForm(forms.Form):
    dish_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name of dish",
                "class": "form-control"
            }
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
            "price",
        )
        widgets = {
            "dishes": forms.CheckboxSelectMultiple(),
            "price": forms.NumberInput(
                attrs={"readonly": "readonly", "id": "id_price"}
            ),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
            self.save_m2m()
            order.price = sum(dish.price for dish in order.dishes.all())
            order.save(update_fields=["price"])
        return order


class OrderSearchForm(forms.Form):
    customer_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by customer name",
                "class": "form-control"
            }
        ),
    )
