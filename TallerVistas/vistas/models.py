from django.db import models

# Create your models here.
class libros (models.Model):
    Nombre = models.CharField(max_length=60)
    Autor = models.CharField(max_length=60)
    Año_Publicacion = models.CharField(max_length=60)
    Editorial = models.CharField(max_length=60)
    