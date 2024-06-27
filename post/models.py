from django.db import models
from pathlib import Path
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
# Create your models here.

def get_image_path(instance,filename):
    return Path('images')/ str(instance.id)/filename

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to='fotos/')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title  # Representación legible del objeto en el admin y en las consultas
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Puedes añadir otros campos según sea necesario, como total, fecha, etc.

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
