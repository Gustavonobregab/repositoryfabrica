from django.db import models


class cnpj(models.Model):
   nomefantasia = models.CharField(max_lenght=60)
   cnpj = models.IntegerField(max_lenght=16)
   cep = models.IntegerField(max_lenght=10)
   municipio = models.CharField(max_lenght=20)
   email = models.CharField(max_lenght=30)
   
   
   def __str__(self):
      return self.cnpj
   
   