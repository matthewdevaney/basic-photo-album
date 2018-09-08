from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Images


class ImageList(generic.ListView):
    model = Images
    template_name_suffix = '_list'


class ImageAdd(CreateView):
    model = Images
    fields = '__all__'
    template_name_suffix = '_add'
