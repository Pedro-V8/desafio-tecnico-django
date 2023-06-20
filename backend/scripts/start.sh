#!/bin/bash

echo '***** MAKING MIGRATIONS *****'
python manage.py makemigrations

echo '***** MIGRATING *****'
python manage.py migrate

echo '***** CREATING ADMIN USER ****'
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root@root.com', 'root')" | python manage.py shell

echo '***** STARTING SERVER ****'
python manage.py runserver 0.0.0.0:8000
