from django.db import models
from recursos.models import Recurso
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from enderecos.models import Endereco
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recurso)
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome