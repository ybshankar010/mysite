#!/bin/bash

./manage.py collectstatic --noinput
# i commit my migration files to git so i dont need to run it on server
# ./manage.py makemigrations app_name
./manage.py makemigrations

./manage.py migrate

echo "Migrations are successfully completed"
gunicorn --reload --bind 0.0.0.0:8000 mysite.wsgi:application

echo "Successfully started server"