from django.shortcuts import render
from django.views.generic.base import TemplateView

# Usando CBV
class HomePageView(TemplateView): # La clase tiene que heredar
    template_name = "core/home.html" # Este atributo define cual es el template

class SamplePageView(TemplateView):
    template_name = "core/sample.html"