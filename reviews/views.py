from django.shortcuts import render
from .models import Review

# Create your views here.


def reviews(request):
    """ A view to return the reviews page """
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/reviews.html', context)
