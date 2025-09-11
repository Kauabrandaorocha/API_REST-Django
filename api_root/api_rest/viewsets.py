from rest_framework import viewsets
from .serializers import EnderecoCepSerializer
from .models import EnderecoCep
import requests

class EnderecoCepViewSet(viewsets.ModelViewSet):
    queryset = EnderecoCep.objects.all()
    serializer_class = EnderecoCepSerializer

    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            serializer.save(
                logradouro=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                localidade=data.get('localidade', ''),
                uf=data.get('uf', '')
            )
        else:
            serializer.save()
            

        return super().perform_create(serializer)