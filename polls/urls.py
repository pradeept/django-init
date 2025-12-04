# custom created, name convention should be followed
# For defining routing info

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
