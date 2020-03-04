from django.urls import include, path

from . import views

app_name = "api"

urlpatterns = [
    path(
        "",
        views.SchemaView.with_ui("redoc", cache_timeout=0),
        name="documentation",
    ),
    path("v1/", include("apps.core.api.v1")),
]
