from django.shortcuts import render
from .models import Workshop

# Create your views here.


def workshops(request):
    context = {
        'workshops': Workshop.objects.all()
    }
    return render(request, 'workshops/workshops.html', context)
