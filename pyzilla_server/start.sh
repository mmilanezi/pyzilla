#! /bin/bash

python manage.py migrate

# Inicia o servidor
python manage.py runserver
python manage.py createsuperuser