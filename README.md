# vaii-semestralka
Semestrálna práca na predmet VAII

![logo](/static/images/page_logo.png)

Stránka je spustitelná na adresách:
1. localhost:8000
2. 127.0.0.1:8000
3. 0.0.0.0:8000

Na spustenie appky v dockeri je potrebné spustiť príkazy:
1. docker-compose run app django-admin startproject backend .
2. docker-compose up

Na otvorenie shellu pre zadavanie prikazov vo vnutri spusteneho kontajnera pouzijeme prikaz:
1. docker exec -it django_container /bin/bash

Po pridani modelov pre databazu je potrebne v docker shelli vykonat prikazy:
1. python manage.py makemigrations
2. python manage.py migrate
