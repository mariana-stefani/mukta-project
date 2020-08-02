from django.shortcuts import render
from django.views.generic import ListView
from .models import Review

# Create your views here.


def reviews(request):
    """ A view to return the reviews page """
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/reviews.html', context)

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']