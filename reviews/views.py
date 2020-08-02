from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Review

# Create your views here.


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        return ('reviews')
