from django.db import models


class Recurso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='recursos', null=True, blank=True)

    def __str__(self):
        return self.nome