from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UsuarioDatos(models.Model):
	usuario = models.OneToOneField(User)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=50)

	def __str__(self):
		return self.usuario
