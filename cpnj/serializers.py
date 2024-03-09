from rest_framework import serializers
from .cnpj import cnpj

class cnpjSerializer(serializers.ModelSerializer):
    class meta: 
        model = cnpj 
        fields = ["id","nomefantasia", "cnpj", "cep", "municipio", "email"]