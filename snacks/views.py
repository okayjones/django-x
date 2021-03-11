from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SnackListView(LoginRequiredMixin, ListView):
    template_name = 'snacks/snack-list.html'
    model = Snack

class SnackDetailView(LoginRequiredMixin, DetailView):
    template_name = 'snacks/snack-detail.html'
    model = Snack

class SnackCreateView(LoginRequiredMixin, CreateView):
    template_name = 'snacks/snack-create.html'
    model = Snack
    fields = ['name', 'description', 'user']

class SnackUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'snacks/snack-update.html'
    model = Snack
    fields = ['name', 'description', 'user']

class SnackDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'snacks/snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')