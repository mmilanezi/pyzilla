#! /bin/bash

pip install django sockets

python manage.py migrate

# Inicia o servidor
python manage.py runserver

