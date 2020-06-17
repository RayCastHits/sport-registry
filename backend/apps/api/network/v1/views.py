from rest_framework import generics
from apps.api.registry.models import Sportsman, SportResult
from apps.api.network.v1.serializers import (
    SportsmanSerializer,
    SportResultSerializer,
)


class SportsmanList(generics.ListCreateAPIView):
    """"""

    queryset = Sportsman.objects.all()
    serializer_class = SportsmanSerializer


class SportResultList(generics.ListCreateAPIView):
    """"""

    queryset = SportResult.objects.all()
    serializer_class = SportResultSerializer
