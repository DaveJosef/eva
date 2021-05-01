from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    nome = models.TextField(null=True)
    telefone = models.TextField(null=True)
    minicurriculo = models.TextField(null=True)
    site = models.TextField(null=True)
    rede_social = models.TextField(null=True)
    eh_palestrante = models.BooleanField(null=True)


class Event(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataHora = models.DateTimeField(auto_now=True)
    urlSite = models.TextField()
    autor = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='CustomUser')

    def get_absolute_url(self):
        return reverse('event_detail')

    def __str__(self):
        return self.nome
