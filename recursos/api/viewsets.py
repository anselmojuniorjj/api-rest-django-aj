from rest_framework.viewsets import ModelViewSet
from recursos.models import Recurso
from .serializers import RecursoSerializer

class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
