from django.urls import path
from . import views

app_name = "registry"

urlpatterns = [
    path("sportsman/", views.SportsmanList.as_view(), name="sportsman-list"),
    # path(
    #     "sportsman/create/",
    #     views.SportsmanCreate.as_view(),
    #     name="sportsman-create",
    # ),
    path(
        "sportsman/<int:pk>",
        views.SportsmanDetail.as_view(),
        name="sportsman-detail",
    ),
    path(
        "sportsman/<int:pk>/update/",
        views.SportsmanUpdate.as_view(),
        name="sportsman-update",
    ),
]
