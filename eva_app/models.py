from django.db import models
from django.conf import settings


class Event(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataHora = models.DateTimeField(auto_now=True)
    urlSite = models.CharField(max_length=300)
    autor = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='CustomUser')

    def get_absolute_url(self):
        return reverse('event_detail')

    def __str__(self):
        return self.nome
