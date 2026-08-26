from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Position, Employee, Dish, Order


def index(request: HttpRequest) -> HttpResponse:
    num_pos = Position.objects.count()
    num_emp = Employee.objects.count()
    num_dis = Dish.objects.count()
    num_ord = Order.objects.count()
    context = {
        "num_pos": num_pos,
        "num_emp": num_emp,
        "num_dis": num_dis,
        "num_ord": num_ord,
    }
    return render(request, "catalog/index.html", context)
