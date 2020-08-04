from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('new/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
