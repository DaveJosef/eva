from django.db import models
from django.conf import settings


class Event(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True)
    data = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True, null=True)
    urlSite = models.CharField(max_length=300, null=True)
    autor = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='CustomUser', null=True)

    def get_absolute_url(self):
        return reverse('event_detail')

    def __str__(self):
        return self.nome
