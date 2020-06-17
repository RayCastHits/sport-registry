from django.urls import path
from .views import SportsmanList, SportResultList

app_name = "network"

urlpatterns = [
    path("sportsman/list/", SportsmanList.as_view()),
    path("sport-result/list/", SportResultList.as_view()),
]
