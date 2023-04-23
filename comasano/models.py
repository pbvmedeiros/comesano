from django.db import models

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