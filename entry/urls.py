from django.urls import path
from . import views

urlpatterns = [
    path("", views.List),
    path("detail/<int:id>",views.detail, name="detail"),
    path("add",views.addNew,name='add-new'),
    path("edit/<int:id>",views.edit, name="edit"),
    path("delete/<int:id>",views.delete, name="delete")
]
