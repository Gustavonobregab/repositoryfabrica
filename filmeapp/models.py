from django.db import models

#criei as models com os dados e limites a serem recebidos para serem importados pro bd

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.CharField(max_length=4)
    diretor = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
   
def __str__(self):
   return self.filme
   
   