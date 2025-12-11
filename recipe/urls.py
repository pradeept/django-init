from django.urls import path

from .views import *

app_name='recipe'

urlpatterns = [
    path("", index, name="index"),
    path("delete_recipe/<int:id>", delete_recipe, name="delete_recipe")
]
