from rest_framework import serializers
from clientes.models import Cliente


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

