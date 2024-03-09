# FilmeApp

O FilmeApp é um aplicativo Django REST que consome dados da API OMDb para buscar informações sobre filmes e armazena esses dados em um banco de dados local. Ele permite aos usuários consultar informações detalhadas de filmes, incluindo título, ano de lançamento, diretor e gênero, diretamente de uma interface API ou via Django Admin.

-------- models---------
O coração do FilmeApp é o modelo Filme, que define a estrutura dos dados a serem armazenados no banco de dados. Cada instância do modelo Filme representa um filme único no banco de dados, com suas informações capturadas pela API OMDb.

--------views-----------

As views no FilmeApp manipulam as requisições HTTP para consumir a API OMDb e armazenar os dados retornados no modelo Filme. Há uma view principal: 

filmes_api: Esta view é responsável por receber o nome de um filme como entrada, consumir a API OMDb para buscar informações sobre o filme e, então, armazenar esses dados no banco de dados usando o modelo Filme. Se bem-sucedido, retorna os dados do filme armazenados; caso contrário, retorna um erro.

------serializers------

 No contexto do FilmeApp,  o FilmeSerializer é responsável por:

Transformar instâncias do modelo Filme em dados JSON para serem enviados nas respostas HTTP.
Validar dados recebidos em formato JSON antes de salvá-los como instâncias do modelo Filme.
O FilmeSerializer garante que os dados enviados e recebidos através das APIs estejam corretamente formatados e validados, facilitando a integração com outros serviços ou aplicações frontend.



Infelizmente näo consegui obter todos os recursos para fazer com que funcione perfeitamente , mas o aprendizado até entäo foi extremamente válido, afinal nunca tive contato com python e django. Acredito que aprendi muito e estou preparado para aprender mais! 
