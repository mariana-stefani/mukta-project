from django.urls import path
from .views import ReviewListView
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
]
