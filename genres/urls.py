from django.contrib import admin
from django.urls import path
from genres.views import GenreUpdateDeleteDetail, GenerCrateListView 


urlpatterns = [
    path('genres/', GenerCrateListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreUpdateDeleteDetail.as_view(), name='detail-genre'),
]