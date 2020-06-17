from django.urls import include, path
from . import views

app_name = "registry"

urlpatterns = [
    path("sportsman/", views.SportsmanList.as_view(), name="sportsman-list"),
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
        "sportsman/<int:pk>/parent/create/",
        views.ParentCreate.as_view(),
        name="parent-create",
    ),
    path(
        "sportsman/<int:pk>/parent/<int:parent_pk>/update/",
        views.ParentUpdate.as_view(),
        name="parent-update",
    ),
    path(
        "sportsman/<int:pk>/primary/create/",
        views.PrimaryCreate.as_view(),
        name="primary-create",
    ),
    path(
        "sportsman/<int:pk>/primary/update/",
        views.PrimaryUpdate.as_view(),
        name="primary-update",
    ),
    path(
        "sportsman/<int:pk>/primary/detail/",
        views.PrimaryDetail.as_view(),
        name="primary-detail",
    ),
    path(
        "sportsman/<int:pk>/medical/create/",
        views.MedicalCreate.as_view(),
        name="medical-create",
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
    path("rating/", views.PrimaryRating.as_view(), name="primary-rating"),
    path(
        "sportsman/<int:pk>/sportresult-primary/create/",
        views.SportResultPrimaryCreate.as_view(),
        name="sportresult-primary-create",
    ),
    path(
        "sportsman/<int:pk>/sportresult-medical/create/",
        views.SportResultMedicalCreate.as_view(),
        name="sportresult-medical-create",
    ),
    path(
        "sportsman/<int:pk>/sportresult-primary/<int:sportrelust_pk>/update/",
        views.SportResultPrimaryUpdate.as_view(),
        name="sportresult-primary-update",
    ),
]
