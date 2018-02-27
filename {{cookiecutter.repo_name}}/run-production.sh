#!/bin/bash

cd /home/django/
python manage.py migrate
python manage.py collectstatic --noinput

uwsgi --ini conf/app.ini
