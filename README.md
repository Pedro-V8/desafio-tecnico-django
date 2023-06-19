# Desafio Técnico Django

Repositório dedicado ao Desafio Técnico para seleção de desenvolvedor Python.


Tecnologias Utiliadas:

- Django
- Django Rest Framework
- Postgres
- React
- Docker


## Instalção e Configuração

Primeiramente será necessário entrar no diretório "backend":

```bash
cd backend/
```

Realizar o build da imagem utiliando docker-compose:

```bash
docker-compose build
```

Por fim subir o container da API:

```bash
docker-compose up
```

Os processos do RabbitMQ e do django-celery irão subir automaticamente, assim como as migrações do banco de dados e o admin-user como root (usuário: root , senha: root).

Agora para iniciar o frontend, abrir um novo terminal e realiar o mesmo processo porém na pasta "frontend":

```bash
cd frontend/
docker-compose build
docker-compose up
```

A API está servida na url: http://localhost:8000/

Já o frontend servido na url: http://localhost:3000/
