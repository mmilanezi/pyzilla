FROM python:3.10-alpine3.18

# Argumentos para o user
ARG user
ARG uid

RUN apk update

# Programas adicionais
RUN apk add bash
RUN apk add nano
RUN apk add vim
RUN apk add openrc
RUN mkdir /run/openrc && touch /run/openrc/softlevel
RUN rc-status

# Nginx
RUN apk add nginx
RUN rc-update add nginx


RUN mkdir -p /home/$user/.composer && \
     chown -R $user:$user /home/$user

RUN chmod -R 777 /var/www
WORKDIR /var/www/

# Comando para copiar o projeto para a pasta correta
COPY . /var/www/
# Comando para copiar as configurações do servidor web
COPY ./vowe.conf /etc/nginx/http.d/default.conf

RUN chown 82:82 -R /var/www/

USER $user