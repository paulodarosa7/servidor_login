from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.TextField(max_length=255)


def __str__(self):
    return f"{self.id_user} | {self.username}"