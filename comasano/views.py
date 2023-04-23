from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Receta

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, 'detalle_receta.html', {'receta': receta})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def exito(request):
    return render(request, 'exito.html')

@method_decorator(login_required, name='dispatch')
class MisRecetasView(ListView):
    model = Receta
    template_name = 'mis_recetas.html'
    context_object_name = 'recetas'

@method_decorator(login_required, name='dispatch')
class CrearRecetaView(CreateView):
    model = Receta
    template_name = 'crear_receta.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'facilidad_preparacion', 'tiempo_preparacion', 'imagen']
    success_url = '/exito'

@method_decorator(login_required, name='dispatch')
class EditarRecetaView(UpdateView):
    model = Receta
    template_name = 'editar_receta.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'facilidad_preparacion', 'tiempo_preparacion', 'imagen']
    success_url = reverse_lazy('mis_recetas')

@method_decorator(login_required, name='dispatch')
class EliminarRecetaView(DeleteView):
    model = Receta
    template_name = 'eliminar_receta.html'
    success_url = reverse_lazy('mis_recetas')