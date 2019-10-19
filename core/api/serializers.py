from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from recursos.api.serializers import RecursoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    # Nested relationships
    atracao = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    recurso = RecursoSerializer(many=True)

    # SerializerMethodField
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'atracao', 'recurso', 'endereco', 'foto',
                  'descricao_completa')


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)