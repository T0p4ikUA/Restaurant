from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import PositionForm, EmployeeForm
from catalog.models import Position, Employee, Dish, Order


def index(request: HttpRequest) -> HttpResponse:
    num_pos = Position.objects.count()
    num_emp = Employee.objects.count()
    num_dis = Dish.objects.count()
    num_ord = Order.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_pos": num_pos,
        "num_emp": num_emp,
        "num_dis": num_dis,
        "num_ord": num_ord,
        "num_visits": num_visits,
    }
    return render(request, "catalog/index.html", context)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "catalog/position_list.html"
    context_object_name = "positions_list"
    queryset = Position.objects.all()


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    template_name = "catalog/position_form.html"
    form_class = PositionForm
    success_url = reverse_lazy("catalog:position-list")


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "catalog/position_detail.html"

class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("catalog:position-list")
    template_name = "catalog/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("catalog:position-list")
    template_name = "catalog/position_confirm_delete.html"


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = "catalog/employee_list.html"
    context_object_name = "employees_list"
    queryset = Employee.objects.select_related("position")
    paginate_by = 3


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    template_name = "catalog/employee_form.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("catalog:employee-list")


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    template_name = "catalog/employee_detail.html"

class EmployeeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("catalog:employee-list")
    template_name = "catalog/employee_form.html"


class EmployeeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("catalog:employee-list")
    template_name = "catalog/employee_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "catalog/dish_list.html"
    context_object_name = "dishes_list"
    queryset = Dish.objects.select_related("cooked_by")
    paginate_by = 3


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "catalog/order_list.html"
    context_object_name = "orders_list"
    queryset = Order.objects.prefetch_related("order_taker")
    paginate_by = 3
