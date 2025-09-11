from rest_framework import serializers
from .models import EnderecoCep

class EnderecoCepSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoCep
        field = ['cep', 'logradouro', 'bairro', 'localidade', 'uf']
        read_only_fields = ['logradouro', 'bairro', 'localidade', 'uf']