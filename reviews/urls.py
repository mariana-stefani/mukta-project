from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('new/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
]
