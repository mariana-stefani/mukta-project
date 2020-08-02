from django.urls import path
from .views import ReviewListView, ReviewCreateView
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('new/', ReviewCreateView.as_view(), name='review-create'),
]
