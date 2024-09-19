from django.urls import path
from movies.views import MovieCreateListView, MovieUpdateDeleteDetail

urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieUpdateDeleteDetail.as_view(), name='detail-movie'),

]