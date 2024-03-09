from django.shortcuts import render
from rest_framework import generics
from .models import cnpj
from serializers import cnpjSerializer

# Create your views here.
class recebercnpjview(generics.ListCreateAPIView):
  queryset = cnpj.objects.all() 
  serializer_class = cnpjSerializer
