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
    path(
        "sportsman/create/",
        views.SportsmanCreate.as_view(),
        name="sportsman-create",
    ),

    path(
        "sportsman/<int:pk>/primary/create/",
        views.PrimaryCreate.as_view(),
        name="primary-create",
    ),
    path(
        "sportsman/<int:pk>/umo/create/",
        views.UMOCreate.as_view(),
        name="umo-create",
    ),

    path("sporttype/", views.SportTypeList.as_view(), name="sporttype-list"),
    path(
        "sporttype/<int:pk>/update/",
        views.SportTypeUpdate.as_view(),
        name="sporttype-update",
    ),
    path(
        "sporttype/create/",
        views.SportTypeCreate.as_view(),
        name="sporttype-create",
    ),
]
