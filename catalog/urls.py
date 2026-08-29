from django.urls import path
from catalog.views import (
    index,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    PositionDetailView,
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeDetailView,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderDetailView,
)

app_name = "catalog"
urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-form"
    ),
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
    path(
        "positions/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),

    path(
        "employees/",
        EmployeeListView.as_view(),
        name="employee-list"
    ),
    path(
        "employees/create/",
        EmployeeCreateView.as_view(),
        name="employee-form"
    ),
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
    path(
        "employees/<int:pk>/",
        EmployeeDetailView.as_view(),
        name="employee-detail"
    ),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-form"),
    path(
        "dishes/<int:pk>/update",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/delete",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),

    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/create/", OrderCreateView.as_view(), name="order-form"),
    path(
        "orders/<int:pk>/update",
        OrderUpdateView.as_view(),
        name="order-update",
    ),
    path(
        "orders/<int:pk>/delete",
        OrderDeleteView.as_view(),
        name="order-delete",
    ),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
