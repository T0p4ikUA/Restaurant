from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
