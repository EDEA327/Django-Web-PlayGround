from django.shortcuts import render
from django.views.generic.base import TemplateView

# Usando CBV
class HomePageView(TemplateView): # La clase tiene que heredar
    template_name = "core/home.html"
    context = {'title': 'Mi Super Web Playground'} # Este atributo define cual es el template
#? Como modificar el diccionario de contexto con una CBV
#* Se debe procesar la respuesta de la vista.
#* La respuesta de la vista se define en el metodo get() si sobreescribimos get()
#* Conseguiremos sobreescribir la respuesta en si misma
#! Se le debe pasar self, request,*args,**kwargs los dos ultimos para buenas prácticas

    def get(self, request):
        return render(request,self.template_name,self.context)
class SamplePageView(TemplateView):
    template_name = "core/sample.html"