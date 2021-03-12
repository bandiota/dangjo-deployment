from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from first_app import models
from django.urls import reverse_lazy

# Create your views here.
 
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'


class MusicianDetail(DetailView):
    ##pk need to mention 
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'


class AddMusician(CreateView):
    ## field name required
    model = models.Musician
    fields = ('first_name', 'last_name', 'instrument')
    template_name = 'first_app/musician_form.html'


class UpdateMusician(UpdateView):
    ## pk required....except all same as createview
    model = models.Musician
    fields = ('first_name', 'last_name', 'instrument')
    template_name = 'first_app/musician_form.html'


class DeleteMusician(DeleteView):
    ## pk required
    ## reverse_lazy does not apply direct delete but wait for furthur confirmation
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('first_app:index')
    template_name = 'first_app/musician_delete.html'