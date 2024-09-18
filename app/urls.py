
from django.contrib import admin
from django.urls import path
from genres.views import ListCrateGenerView, DetailUpdateDelete
from actors.views import ActorUpdateDeleteDetail, ActorCreateListView 
from movies.views import MovieUpdateDeleteDetail, MovieCreateListView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', ListCrateGenerView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', DetailUpdateDelete.as_view(), name='detail-genre'),

    path('actors/', ActorCreateListView.as_view(),name='actor-list'),
    path('actors/<int:pk>/', ActorUpdateDeleteDetail.as_view(),name='detail-list'),

    path('movies/', MovieCreateListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieUpdateDeleteDetail.as_view(), name='detail-list')


]
