from django.db import models

# Create your models here.


class Event(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataHora = models.DateTimeField(auto_now=True)
    urlSite = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('event_detail')

    def __str__(self):
        return self.nome
