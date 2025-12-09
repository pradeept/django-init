# custom created, name convention should be followed
# For defining routing info

from django.urls import path

from . import views

# namespace
# defining namespace helps in referencing a path in href and other places.
app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # Using Generic View
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
