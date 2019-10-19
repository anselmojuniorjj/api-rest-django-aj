from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # habilita buscas
    filter_backends = [SearchFilter]
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', 'endereco__linha1']

    # altera o comportamento padrão(busca por id)
    # lookup_field = 'nome'

    # def get_queryset(self):
    #     id = self.request.query_params.get('id', None)
    #     nome = self.request.query_params.get('nome', None)
    #     descricao = self.request.query_params.get('descricao', None)
    #     queryset = PontoTuristico.objects.all()
    #
    #     if id:
    #         queryset = PontoTuristico.objects.filter(pk=id)
    #
    #     if nome:
    #         queryset = queryset.filter(nome__iexact=nome)
    #
    #     if descricao:
    #         queryset = queryset.filter(descricao__iexact=descricao)
    #
    #     return queryset
    #     #return PontoTuristico.objects.filter(aprovado=True)

    '''
        Sobrescrever a action do GET
    '''

    def list(self, request, *args, **kwargs):
        # fazer query, cálculos, validar permissões, etc e dar retorno necessário
        # return Response({'teste': 123})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    '''
           Sobrescrever a action do POST
    '''
    # def create(self, request, *args, **kwargs):
    #     # fazer query, cálculos, validar permissões, etc e dar retorno necessário
    #     return Response({'Hello ': request.data['nome']})

    '''
           Sobrescrever a action do DELETE
    '''
    # def destroy(self, request, *args, **kwargs):
    #     # fazer query, cálculos, validar permissões, etc e dar retorno necessário
    #     return Response({'Hello ': request.data['nome']})

    '''
            Sobrescrever a action do RETRIEVE (GET - retorna um valor por ID)
    '''
    # def retrieve(self, request, *args, **kwargs):
    #     # fazer query, cálculos, validar permissões, etc e dar retorno necessário
    #     return Response({'Hello ': request.data['nome']})

    '''
            Sobrescrever a action do UPDATE (método PUT)
    '''
    # def update(self, request, *args, **kwargs):
    #     # fazer query, cálculos, validar permissões, etc e dar retorno necessário
    #     return Response({'Hello ': request.data['nome']})

    '''
            Sobrescrever a action do PARTIAL_UPDATE (método PATCH)
    '''
    # def partial_update(self, request, *args, **kwargs):
    #     # fazer query, cálculos, validar permissões, etc e dar retorno necessário
    #     return Response({'Hello ': request.data['nome']})

    '''
        CRIAR UMA ACTION PERSONALIZADA
        para acessar esse método url:
        pontosturisticos/id/denunciar
    '''

    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    '''
        CRIAR UMA ACTION PERSONALIZADA
        para acessar esse método url:
        pontosturisticos/teste
    '''

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass