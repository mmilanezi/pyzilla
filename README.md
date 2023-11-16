# Projeto Pyzilla
Projeto de transferência de arquivos com Python utilizando sockets

## Bibliotecas utilizadas

- Django

## Comandos de administração

Caso seja necessário acessar o portal admin, devemos criar uma contad e administrador.
Usamos o comando:
python manage.py createsuperuser

## Estrutura do projeto

Na pasta pyzilla_client é onde fica toda a lógica da interface de client do sistema. Em pyzilla_root fica a pasta raiz do projeto django onde fica as rotas e configurações. 
Em pyzilla_server fica toda a logica de sockets e transferência de arquivos entre os clientes.