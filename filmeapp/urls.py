from django.urls import path
from . import views

urlpatterns = [
    # sua outra configuração de URL...
    path('filmes/', views.filmes_api, name='filmes_api'),
]
