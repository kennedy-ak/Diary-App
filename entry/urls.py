from django.urls import path
from . import views

urlpatterns = [
    path("", views.List),
    path("detail/<int:id>",views.detail, name="detail")
]
