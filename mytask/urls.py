from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("task/<int:pk>/add", views.add, name="add"),
    path("task/<int:pk>/delete", views.delete, name="delete"),
]
