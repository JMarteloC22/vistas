from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
# importacion de forms, reverse y messages, OJO!!!
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import libros

class CrearLibro(SuccessMessageMixin,CreateView):
    model = libros
    form = libros
    fields = "__all__"
    success_message = 'Libro Creado Correctamente !'

class ListarLibros(ListView):
    model = libros

class DetalleLibro(DetailView):
    model = libros

class ActualizarLibros(SuccessMessageMixin, UpdateView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        return reverse('leer')
    
class EliminarLibro (SuccessMessageMixin, DeleteView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        success_message = 'Libro Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')