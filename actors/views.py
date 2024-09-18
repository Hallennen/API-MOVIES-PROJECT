from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from actors import models, serializers


# Create your views here.


class ActorCreateListView(ListCreateAPIView):
    queryset = models.Actors.objects.all()
    serializer_class = serializers.ActorsSerializers


class ActorUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Actors.objects.all()
    serializer_class = serializers.ActorsSerializers