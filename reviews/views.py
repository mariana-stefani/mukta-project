from django.shortcuts import render
from django.views.generic import ListView
from .models import Review

# Create your views here.

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']