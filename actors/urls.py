from django.urls import path
from actors.views import ActorUpdateDeleteDetail, ActorCreateListView


urlpatterns = [
    path('actors/', ActorCreateListView.as_view(),name='actor-list'),
    path('actors/<int:pk>/', ActorUpdateDeleteDetail.as_view(),name='detail-actor'),

]