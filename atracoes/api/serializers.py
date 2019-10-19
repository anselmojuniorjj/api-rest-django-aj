from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'atracao', 'descricao', 'horario_func',
                 'data', 'foto')