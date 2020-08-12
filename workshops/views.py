from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Workshop

# Create your views here.


class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshops/workshops.html'
    context_object_name = 'workshops'


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/workshop-detail.html'
    context_object_name = 'workshop-detail'


class WorkshopCreateView(UserPassesTestMixin, CreateView):
    model = Workshop
    template_name = 'workshops/workshop-form.html'
    context_object_name = 'workshop-create'
    fields = ['title', 'date', 'location',
              'time', 'instructor', 'content', 'images']
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser


class WorkshopUpdateView(UserPassesTestMixin, UpdateView):
    model = Workshop
    template_name = 'workshops/workshop-form.html'
    context_object_name = 'workshop-update'
    fields = ['title', 'date', 'location',
              'time', 'instructor', 'content', 'images']
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser


class WorkshopDeleteView(UserPassesTestMixin, DeleteView):
    model = Workshop
    template_name = 'workshops/workshop-delete.html'
    context_object_name = 'workshop-delete'
    success_url = '/workshops'

    def test_func(self):
        return self.request.user.is_superuser
