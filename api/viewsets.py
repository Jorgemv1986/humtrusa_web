from rest_framework import viewsets
from api.serializer import ClientesSerializer
from clientes.models import Cliente


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
