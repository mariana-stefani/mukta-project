from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Review

# Create your views here.


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'workshops/review-form.html'
    context_object_name = 'review-create'
    fields = ['title', 'content']
    success_url = '/reviews'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'workshops/review-detail.html'
    context_object_name = 'review-detail'


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        return ('reviews')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review-delete.html'
    context_object_name = 'review-delete'
    success_url = '/reviews'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewUserView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'reviews/user-reviews.html'
    ordering = ['-date_posted']
