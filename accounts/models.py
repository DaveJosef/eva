from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    minicurriculo = models.TextField(blank=True)
    site = models.CharField(max_length=300, blank=True)
    rede_social = models.CharField(max_length=300, blank=True)
    eh_palestrante = models.BooleanField(blank=True, default=False)
