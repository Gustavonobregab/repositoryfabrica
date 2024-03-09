from rest_framework import serializers
from .models import Filme

#filtrando os dados 

class FilmeSerializer(serializers.ModelSerializer):
    class meta: 
        model = Filme
        fields = ["id","titulo", "ano", "diretor", "genero"]