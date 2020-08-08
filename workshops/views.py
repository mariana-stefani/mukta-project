from django.shortcuts import render
from django.views.generic import ListView
from .models import Workshop

# Create your views here.

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshops/workshops.html'
    context_object_name = 'workshops'