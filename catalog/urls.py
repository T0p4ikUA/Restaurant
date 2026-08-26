from django.urls import path
from catalog.views import (
    index,
    PositionListView,
    EmployeeListView,
    DishListView,
    OrderListView

)

app_name = "catalog"
urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]
