from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import (
    DishForm,
    DishSearchForm,
    EmployeeForm,
    EmployeeSearchForm,
    OrderForm,
    OrderSearchForm,
    PositionForm,
    PositionSearchForm,
)
from catalog.models import Dish, Employee, Order, Position


def index(request):
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
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PositionSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data.get("name"):
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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
    form_class = PositionForm
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
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = EmployeeSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Employee.objects.select_related("position")
        form = EmployeeSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data.get("username"):
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


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
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_name = self.request.GET.get("dish_name", "")
        context["search_form"] = DishSearchForm(
            initial={"dish_name": dish_name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("cooked_by")
        form = DishSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data.get("dish_name"):
            return queryset.filter(
                dish_name__icontains=form.cleaned_data["dish_name"]
            )
        return queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    template_name = "catalog/dish_form.html"
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "catalog/dish_detail.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish-list")
    template_name = "catalog/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("catalog:dish-list")
    template_name = "catalog/dish_confirm_delete.html"


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "catalog/order_list.html"
    context_object_name = "orders_list"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_name = self.request.GET.get("customer_name", "")
        context["search_form"] = OrderSearchForm(
            initial={"customer_name": customer_name}
        )
        return context

    def get_queryset(self):
        queryset = Order.objects.all().prefetch_related("dishes")
        form = OrderSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data.get("customer_name"):
            return queryset.filter(
                customer_name__icontains=form.cleaned_data["customer_name"]
            )
        return queryset


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = "catalog/order_form.html"
    form_class = OrderForm
    success_url = reverse_lazy("catalog:order-list")


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = "catalog/order_detail.html"


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("catalog:order-list")
    template_name = "catalog/order_form.html"


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("catalog:order-list")
    template_name = "catalog/order_confirm_delete.html"
