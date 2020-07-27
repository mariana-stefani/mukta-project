from django.shortcuts import render

# Create your views here.

posts = [
    {
        'username': 'Mari',
        'title': 'First Review',
        'content': 'Great service',
        'date_posted': 'July 27, 2020'
    },
    {
        'username': 'Test',
        'title': 'Second Review',
        'content': 'Loved the service',
        'date_posted': 'July 24, 2020'
    }
]


def reviews(request):
    """ A view to return the reviews page """
    context = {
        'posts': posts
    }
    return render(request, 'reviews/reviews.html', context)
