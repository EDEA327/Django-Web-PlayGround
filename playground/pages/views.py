from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']