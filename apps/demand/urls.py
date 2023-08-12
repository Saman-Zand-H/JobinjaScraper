from django.urls import path

from . import views


app_name = "demand"

urlpatterns = [
    path(
        route="",
        view=views.HomeView.as_view(),
        name="home"
    )
]