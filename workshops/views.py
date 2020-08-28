from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Workshop


class WorkshopListView(ListView):
    """ A view to display all workshops on the workshops page """
    model = Workshop
    template_name = 'workshops/workshops.html'
    context_object_name = 'workshops'
    paginate_by = 5


class WorkshopDetailView(DetailView):
    """ A view to display a single workshop on workshop-detail page """
    model = Workshop
    template_name = 'workshops/workshop-detail.html'
    context_object_name = 'workshop-detail'


class WorkshopCreateView(UserPassesTestMixin, CreateView):
    """ A view to create a new workshop on workshop-form page """
    model = Workshop
    template_name = 'workshops/workshop-form.html'
    context_object_name = 'workshop-create'
    fields = ['title', 'date', 'location',
              'time', 'instructor', 'content', 'images', 'order', 'divider']
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser


class WorkshopUpdateView(UserPassesTestMixin, UpdateView):
     """ A view to update a workshop on workshop-form page """
    model = Workshop
    template_name = 'workshops/workshop-form.html'
    context_object_name = 'workshop-update'
    fields = ['title', 'date', 'location',
              'time', 'instructor', 'content', 'images', 'order', 'divider']
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser


class WorkshopDeleteView(UserPassesTestMixin, DeleteView):
    """ A view to delete a workshop on workshop-delete page """
    model = Workshop
    template_name = 'workshops/workshop-delete.html'
    context_object_name = 'workshop-delete'
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser
