from django.db import models

# Create your models here.
class EnderecoCep(models.Model):
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Rua: {self.logradouro}, Bairro: {self.bairro}, Cidade: {self.localidade}, Estado: {self.uf}, CEP: {self.cep}"