from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:orderid>/", views.orders_view, name="orders_view"),
]