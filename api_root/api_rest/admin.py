from django.contrib import admin
from .models import EnderecoCep

class EnderecoCepAdmin(admin.ModelAdmin):
    search_fields = ['cep']

admin.site.register(EnderecoCep, EnderecoCepAdmin)