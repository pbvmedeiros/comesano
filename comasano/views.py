from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView

from django.views.generic import ListView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Receta, Profile, Mensaje

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

class MisRecetasView(LoginRequiredMixin, ListView):
    model = Receta
    template_name = 'mis_recetas.html'
    context_object_name = 'recetas'

class CrearRecetaView(LoginRequiredMixin, CreateView):
    model = Receta
    template_name = 'crear_receta.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'facilidad_preparacion', 'tiempo_preparacion', 'imagen']
    success_url = '/exito'

class EditarRecetaView(LoginRequiredMixin, UpdateView):
    model = Receta
    template_name = 'editar_receta.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'facilidad_preparacion', 'tiempo_preparacion', 'imagen']
    success_url = reverse_lazy('mis_recetas')

class EliminarRecetaView(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name = 'eliminar_receta.html'
    success_url = reverse_lazy('mis_recetas')


class Login(LoginView):
    next_page = reverse_lazy("home")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

class Logout(LogoutView):
    template_name = "salir.html"


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("home")
    fields = ['avatar','acerca', 'mi_email',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("home")
    fields = ['avatar','acerca', 'mi_email',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()


class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()
    
