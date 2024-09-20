from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from reviews.models import Review
from reviews.serializers import ReviewSerializers
from rest_framework.permissions import IsAuthenticated  



# Create your views here.
class ReviewCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers