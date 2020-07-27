from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reviews(request):
    """ A view to return the reviews page """
    
    return render(request, 'reviews/reviews.html')