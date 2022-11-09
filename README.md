# vaii-semestralka
Semestrálna práca na predmet VAII

Na spustenie appky v dockeri je potrebné prepnúť branch na backend, a následne spustiť príkazy:
1. docker-compose run app django-admin startproject backend .
2. docker-compose up

Na otvorenie shellu pre zadavanie prikazov vo vnutri spusteneho kontajnera pouzijeme prikaz:
1. docker exec -it django_container /bin/bash

Po pridani modelov pre databazu je potrebne v docker shelli vykonat prikazy:
1. python manage.py makemigrations
2. python manage.py migrate
