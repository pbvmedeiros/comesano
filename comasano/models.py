from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    facilidad_preparacion = models.CharField(max_length=50)
    tiempo_preparacion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='recetas/')

    def __str__(self):
        return self.titulo
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    acerca = models.TextField()
    mi_email= models.CharField(max_length=100)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''


class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    fecha = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")