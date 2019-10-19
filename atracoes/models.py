from django.db import models


class Atracao(models.Model):
    atracao = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    data = models.DateTimeField(null=True, blank=True)
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.atracao