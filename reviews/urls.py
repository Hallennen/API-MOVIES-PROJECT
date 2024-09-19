from django.urls import path
from reviews.views import ReviewCreateListView, ReviewUpdateDeleteDetail


urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='review-list' ),
    path('reviews/<int:pk>/', ReviewUpdateDeleteDetail.as_view(), name='detail-review'),

]