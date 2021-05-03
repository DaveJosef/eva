from django.db import models
from django.conf import settings


class OuvinteEvento(models.Model):
    usuario = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='CustomUserOuvinte')
    evento = models.ForeignKey(to=settings.EVENT_MODEL,
                              on_delete=models.CASCADE, related_name='EventoInscrito')

    def get_absolute_url(self):
        return reverse('inscricao')

    def __str__(self):
        return self.evento


class PalestranteEvento(models.Model):
    usuario = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='CustomUserPalestrante')
    evento = models.ForeignKey(to=settings.EVENT_MODEL,
                              on_delete=models.CASCADE, related_name='EventoPalestrado')

    def get_absolute_url(self):
        return reverse('palestra')

    def __str__(self):
        return self.evento
