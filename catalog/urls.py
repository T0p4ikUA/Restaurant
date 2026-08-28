from django.urls import path
from catalog.views import (
    index,
    PositionListView,
    EmployeeListView,
    DishListView,
    OrderListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    PositionDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeDetailView,
)

app_name = "catalog"
urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-form"),
    path(
        "positions/<int:pk>/update",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),


    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-form"),
    path(
        "employees/<int:pk>/update",
        EmployeeUpdateView.as_view(),
        name="employee-update",
    ),
    path(
        "employees/<int:pk>/delete",
        EmployeeDeleteView.as_view(),
        name="employee-delete",
    ),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]
