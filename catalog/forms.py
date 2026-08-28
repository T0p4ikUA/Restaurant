from django import forms

from catalog.models import Position, Employee


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("username", "position", "is_active")