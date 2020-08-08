from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Workshop

# Create your views here.


@login_required
def workshops(request):
    context = {
        'workshops': Workshop.objects.all()
    }
    return render(request, 'workshops/workshops.html', context)
