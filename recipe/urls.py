from django.urls import path

from .views import *

app_name='recipe'

urlpatterns = [
    path("", index, name="index"),
]
