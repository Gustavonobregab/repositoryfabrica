from filmeapp.urls import path


urlpatterns = [
    path('', views.index, name = 'index')
] 

