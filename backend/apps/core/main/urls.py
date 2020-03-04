from django.urls import path, include

from . import views


urlpatterns = [
    path("api/", include("apps.core.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("pages/", include("django.contrib.flatpages.urls")),
    path("", views.HomeView.as_view(), name="home"),
    path("<slug:template>/", views.PageLoaderView.as_view(), name="page"),
]
