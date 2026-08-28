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
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]
