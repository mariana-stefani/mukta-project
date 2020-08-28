from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Review


class ReviewListView(ListView):
    """ A view to display all reviews on the reviews page """
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']
    paginate_by = 5


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ A view to create a new review on review-form page """
    model = Review
    template_name = 'reviews/review-form.html'
    context_object_name = 'review-create'
    fields = ['title', 'content']
    success_url = '/reviews'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDetailView(DetailView):
    """ A view to display a single review on review-detail page """
    model = Review
    template_name = 'reviews/review-detail.html'
    context_object_name = 'review-detail'


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A view to update a review on review-form page """
    model = Review
    fields = ['title', 'content']
    template_name = 'reviews/review-form.html'
    context_object_name = 'review-update'
    success_url = '/reviews'

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
    """ A view to delete a review on review-delete page """
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
    """ A view to display all reviews from user on user-reviews page """
    model = Review
    context_object_name = 'reviews'
    template_name = 'reviews/user-reviews.html'
    ordering = ['-date_posted']
    paginate_by = 5
