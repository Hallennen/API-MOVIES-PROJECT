from django.shortcuts import render
from movies.serializers import MoviesSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from movies import models

# Create your views here.
class MovieCreateListView(ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = MoviesSerializers


class MovieUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = MoviesSerializers